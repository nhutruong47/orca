import json
import os
import urllib.error
import urllib.request
from typing import Any

BASE_URL = os.getenv("AI_SERVICE_URL", "http://127.0.0.1:8000")


def request_json(method: str, path: str, payload: dict[str, Any] | None = None) -> tuple[int, dict[str, Any]]:
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(BASE_URL + path, data=data, method=method, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            body = response.read().decode("utf-8")
            return response.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(body)
        except json.JSONDecodeError:
            parsed = {"raw": body}
        return exc.code, parsed


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def print_json(title: str, value: Any) -> None:
    print(f"\n=== {title} ===")
    print(json.dumps(value, ensure_ascii=False, indent=2))


def normalize(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False).lower()


def assert_contains_all(text: str, keywords: list[str], label: str) -> None:
    missing = [keyword for keyword in keywords if keyword.lower() not in text]
    assert_true(not missing, f"{label} missing keywords: {missing}")


def assert_contains_any(text: str, alternatives: list[str], label: str) -> None:
    assert_true(
        any(alternative.lower() in text for alternative in alternatives),
        f"{label} missing any of: {alternatives}",
    )


def context_from_extract(original_text: str, extract: dict[str, Any]) -> dict[str, Any]:
    return {
        "mode": "WAITING_CLARIFICATION",
        "originalText": original_text,
        "intent": extract["intent"],
        "previousFields": extract["fields"],
        "missingFields": extract["missingFields"],
    }


def demo_members() -> list[dict[str, Any]]:
    return [
        {"userId": "member-material", "username": "material01", "fullName": "Anh Nguyên Liệu", "jobLabels": ["nguyen lieu", "blend", "san xuat"]},
        {"userId": "member-rang", "username": "rang01", "fullName": "Anh Rang", "jobLabels": ["rang", "medium roast", "agtron", "san xuat"]},
        {"userId": "member-xay", "username": "xay01", "fullName": "Chị Xay", "jobLabels": ["xay", "pha phin", "micron"]},
        {"userId": "member-qc", "username": "qc01", "fullName": "Bạn QC", "jobLabels": ["qc", "kiem tra", "chat luong", "do am"]},
        {"userId": "member-pack", "username": "pack01", "fullName": "Chị Đóng Gói", "jobLabels": ["dong goi", "bao bi", "tem nhan", "dong thung"]},
    ]


def run_state_machine_context_case() -> None:
    initial_payload = {"teamId": "demo-team", "text": "Sản xuất 100kg trước chiều mai"}
    status1, extract1 = request_json("POST", "/extract", initial_payload)
    print_json("TC01 EXTRACT - MISSING PRODUCT", {"status": status1, "request": initial_payload, "response": extract1})
    assert_true(status1 == 200, "TC01 initial extract should return 200")
    assert_true(extract1.get("intent") == "PRODUCTION_PLAN", "TC01 initial intent should be PRODUCTION_PLAN")
    assert_true("productName" in extract1.get("missingFields", []), "TC01 should ask for productName")
    assert_true(extract1.get("fields", {}).get("quantity") == 100, "TC01 should keep quantity=100")
    assert_true(extract1.get("fields", {}).get("unit") == "kg", "TC01 should keep unit=kg")
    assert_true(extract1.get("fields", {}).get("deadline"), "TC01 should resolve deadline")

    followup_payload = {
        "teamId": "demo-team",
        "text": "Arabica",
        "context": {
            "mode": "WAITING_CLARIFICATION",
            "originalText": initial_payload["text"],
            "intent": extract1["intent"],
            "previousFields": extract1["fields"],
            "missingFields": extract1["missingFields"],
        },
    }
    status2, extract2 = request_json("POST", "/extract", followup_payload)
    print_json("TC01 EXTRACT - CONTINUE WITH CONTEXT", {"status": status2, "request": followup_payload, "response": extract2})
    fields2 = extract2.get("fields", {})
    assert_true(status2 == 200, "TC01 follow-up extract should return 200")
    assert_true(extract2.get("intent") == "PRODUCTION_PLAN", "TC01 follow-up intent should preserve PRODUCTION_PLAN")
    assert_true(extract2.get("missingFields") == [], "TC01 follow-up should clear missingFields")
    assert_true(fields2.get("productName") == "Arabica", "TC01 follow-up should set productName=Arabica")
    assert_true(fields2.get("quantity") == 100, "TC01 follow-up should preserve quantity=100")
    assert_true(fields2.get("unit") == "kg", "TC01 follow-up should preserve unit=kg")
    assert_true(fields2.get("deadline") == extract1.get("fields", {}).get("deadline"), "TC01 follow-up should preserve deadline")

    plan_payload = {
        "teamId": "demo-team",
        "intent": extract2["intent"],
        "fields": fields2,
        "members": [
            {"userId": "member-rang", "username": "rang01", "fullName": "Anh Rang", "jobLabels": ["rang", "san xuat"]},
            {"userId": "member-pack", "username": "pack01", "fullName": "Chị Đóng Gói", "jobLabels": ["dong goi"]},
        ],
    }
    status3, plan = request_json("POST", "/plan", plan_payload)
    print_json("TC01 PLAN - REAL GEMINI", {"status": status3, "request": plan_payload, "response": plan})
    assert_true(status3 == 200, "TC01 plan should return 200")
    assert_true(plan.get("tasks"), "TC01 plan should include tasks")
    assert_true(plan.get("deadline") == fields2.get("deadline"), "TC01 plan should preserve extracted deadline")


def run_context_memory_cases() -> None:
    print("\n=== CTX01 covered by TC01 state-machine case ===")

    ctx02_text = "Vệ sinh khu đóng gói"
    status1, extract1 = request_json("POST", "/extract", {"teamId": "demo-team", "text": ctx02_text})
    print_json("CTX02 STEP 1 - OPERATION MISSING DEADLINE", {"status": status1, "response": extract1})
    assert_true(status1 == 200, "CTX02 step 1 should return 200")
    assert_true(extract1.get("intent") == "OPERATION_TASK", "CTX02 intent should be OPERATION_TASK")
    assert_true("deadline" in extract1.get("missingFields", []), "CTX02 should ask for deadline")

    status2, extract2 = request_json("POST", "/extract", {
        "teamId": "demo-team",
        "text": "16:30 hôm nay",
        "context": context_from_extract(ctx02_text, extract1),
    })
    print_json("CTX02 STEP 2 - OPERATION DEADLINE FOLLOW-UP", {"status": status2, "response": extract2})
    fields2 = extract2.get("fields", {})
    assert_true(status2 == 200, "CTX02 step 2 should return 200")
    assert_true(extract2.get("intent") == "OPERATION_TASK", "CTX02 should preserve OPERATION_TASK")
    assert_true(extract2.get("missingFields") == [], "CTX02 should clear missingFields")
    assert_true("vệ sinh" in normalize(fields2), "CTX02 should preserve cleaning title")
    assert_true("16:30" in str(fields2.get("deadline", "")), "CTX02 should set deadline 16:30")

    ctx03_text = "Rang Robusta trước thứ Sáu"
    status3, extract3 = request_json("POST", "/extract", {"teamId": "demo-team", "text": ctx03_text})
    print_json("CTX03 STEP 1 - PRODUCTION MISSING QUANTITY", {"status": status3, "response": extract3})
    assert_true(status3 == 200, "CTX03 step 1 should return 200")
    assert_true(extract3.get("intent") == "PRODUCTION_PLAN", "CTX03 intent should be PRODUCTION_PLAN")
    assert_true("quantity" in extract3.get("missingFields", []), "CTX03 should ask for quantity")

    status4, extract4 = request_json("POST", "/extract", {
        "teamId": "demo-team",
        "text": "200kg",
        "context": context_from_extract(ctx03_text, extract3),
    })
    print_json("CTX03 STEP 2 - QUANTITY FOLLOW-UP", {"status": status4, "response": extract4})
    fields4 = extract4.get("fields", {})
    assert_true(status4 == 200, "CTX03 step 2 should return 200")
    assert_true(extract4.get("missingFields") == [], "CTX03 should clear missingFields")
    assert_true(fields4.get("productName") == "Robusta", "CTX03 should preserve productName=Robusta")
    assert_true(fields4.get("quantity") == 200, "CTX03 should set quantity=200")
    assert_true(fields4.get("unit") == "kg", "CTX03 should set unit=kg")

    ctx04_text = "Sản xuất 100kg Arabica"
    status5, extract5 = request_json("POST", "/extract", {"teamId": "demo-team", "text": ctx04_text})
    print_json("CTX04 STEP 1 - PRODUCTION MISSING DEADLINE", {"status": status5, "response": extract5})
    assert_true(status5 == 200, "CTX04 step 1 should return 200")
    assert_true(extract5.get("intent") == "PRODUCTION_PLAN", "CTX04 intent should be PRODUCTION_PLAN")
    assert_true("deadline" in extract5.get("missingFields", []), "CTX04 should ask for deadline")

    status6, extract6 = request_json("POST", "/extract", {
        "teamId": "demo-team",
        "text": "Đổi thành Robusta, trước 17:00 hôm nay",
        "context": context_from_extract(ctx04_text, extract5),
    })
    print_json("CTX04 STEP 2 - CORRECTION AND DEADLINE FOLLOW-UP", {"status": status6, "response": extract6})
    fields6 = extract6.get("fields", {})
    assert_true(status6 == 200, "CTX04 step 2 should return 200")
    assert_true(extract6.get("missingFields") == [], "CTX04 should clear missingFields")
    assert_true(fields6.get("productName") == "Robusta", "CTX04 should update productName=Robusta")
    assert_true(fields6.get("quantity") == 100, "CTX04 should preserve quantity=100")
    assert_true(fields6.get("unit") == "kg", "CTX04 should preserve unit=kg")
    assert_true("17:00" in str(fields6.get("deadline", "")), "CTX04 should set deadline 17:00")

    ctx05_fields = {
        "title": "Sản xuất 100kg Arabica trước chiều mai",
        "productName": "Arabica",
        "quantity": 100,
        "unit": "kg",
        "deadline": "2026-06-21T14:00:00",
    }
    status7, plan = request_json("POST", "/plan", {
        "teamId": "demo-team",
        "intent": "PRODUCTION_PLAN",
        "fields": ctx05_fields,
        "members": demo_members(),
    })
    print_json("CTX05 STEP 1 - CREATE ACTIVE DRAFT", {"status": status7, "response": plan})
    assert_true(status7 == 200, "CTX05 plan should return 200")
    assert_true(plan.get("tasks"), "CTX05 plan should include tasks")

    status8, revised = request_json("POST", "/revise", {
        "teamId": "demo-team",
        "instruction": "Rút gọn còn 2 task và tăng ưu tiên task rang",
        "draft": plan,
        "members": demo_members(),
    })
    print_json("CTX05 STEP 2 - REVISE ACTIVE DRAFT", {"status": status8, "response": revised})
    assert_true(status8 == 200, "CTX05 revise should return 200")
    assert_true(len(revised.get("tasks", [])) == 2, "CTX05 revised draft should have 2 tasks")
    assert_true(revised.get("deadline") == plan.get("deadline"), "CTX05 revise should preserve deadline")
    assert_true("arabica" in normalize(revised), "CTX05 revise should preserve draft topic")


def run_detailed_order_case() -> None:
    order_text = """
Đơn hàng: Gia công 10 tấn cà phê đóng gói
Mã đơn hàng: PO-20260620-001

Thông tin sản phẩm
Tên sản phẩm: Cà phê Blend Robusta Arabica
Thành phần: 70% Robusta 30% Arabica
Nguồn nguyên liệu: Robusta Đắk Lắk Arabica Cầu Đất
Mức rang: Medium Roast
Màu rang mục tiêu: Agtron 55 - 60
Kiểu xay: Xay pha phin
Độ mịn mục tiêu: 500 - 800 micron
Hương vị mong muốn: Hương chocolate Hậu vị ngọt Độ đắng trung bình Ít chua

Khối lượng sản xuất
Thành phẩm yêu cầu: 10.000 kg
Quy cách đóng gói: Túi 500g
Số lượng thành phẩm dự kiến: 20.000 túi

Bao bì
Loại bao bì: Túi kraft van 1 chiều
Kích thước: 500g
Tem nhãn: Tem màu In logo khách hàng
Đóng thùng: 20 túi/thùng carton

Yêu cầu chất lượng
Độ ẩm thành phẩm: ≤ 5%
Tỷ lệ lỗi đóng gói: < 0.5%
Trọng lượng sai số: ±2g
Tỷ lệ hạt cháy: < 1%

Thời gian thực hiện
Ngày bắt đầu: 20/06/2026
Ngày giao hàng: 30/06/2026
""".strip()

    extract_payload = {"teamId": "demo-team", "text": order_text}
    status1, extract = request_json("POST", "/extract", extract_payload)
    print_json("TC02 EXTRACT - DETAILED PRODUCTION ORDER", {"status": status1, "request": extract_payload, "response": extract})
    fields = extract.get("fields", {})
    fields_text = normalize(fields)
    assert_true(status1 == 200, "TC02 extract should return 200")
    assert_true(extract.get("intent") == "PRODUCTION_PLAN", "TC02 intent should be PRODUCTION_PLAN")
    assert_true(extract.get("missingFields") == [], "TC02 should not miss required fields")
    assert_true("30" in str(fields.get("deadline", "")) and "2026" in str(fields.get("deadline", "")), "TC02 deadline should use delivery date 30/06/2026")

    plan_payload = {
        "teamId": "demo-team",
        "intent": extract["intent"],
        "fields": fields,
        "members": [
            {"userId": "member-material", "username": "material01", "fullName": "Anh Nguyên Liệu", "jobLabels": ["nguyen lieu", "blend", "san xuat"]},
            {"userId": "member-rang", "username": "rang01", "fullName": "Anh Rang", "jobLabels": ["rang", "medium roast", "agtron", "san xuat"]},
            {"userId": "member-xay", "username": "xay01", "fullName": "Chị Xay", "jobLabels": ["xay", "pha phin", "micron"]},
            {"userId": "member-qc", "username": "qc01", "fullName": "Bạn QC", "jobLabels": ["qc", "kiem tra", "chat luong", "do am"]},
            {"userId": "member-pack", "username": "pack01", "fullName": "Chị Đóng Gói", "jobLabels": ["dong goi", "bao bi", "tem nhan", "dong thung"]},
        ],
    }
    status2, plan = request_json("POST", "/plan", plan_payload)
    print_json("TC02 PLAN - DETAILED PRODUCTION ORDER", {"status": status2, "request": plan_payload, "response": plan})
    assert_true(status2 == 200, "TC02 plan should return 200")
    tasks = plan.get("tasks", [])
    assert_true(6 <= len(tasks) <= 12, "TC02 detailed plan should return 6..12 tasks")


def main() -> int:
    health_status, health = request_json("GET", "/health")
    print_json("HEALTH", {"status": health_status, "body": health})
    assert_true(health_status == 200, "AI service is not reachable")
    assert_true(health.get("mode") == "gemini", "AI_V2_MODE must be gemini for this test")

    run_state_machine_context_case()
    run_context_memory_cases()
    run_detailed_order_case()

    print("\nRESULT=PASS Gemini context-memory and detailed order cases work.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"\nRESULT=FAIL {exc}")
        raise SystemExit(1)
