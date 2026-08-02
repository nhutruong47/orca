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
        with urllib.request.urlopen(req, timeout=120) as response:
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


def test_case_1_semantic_match() -> None:
    members = [
        {"userId": "w1", "username": "Worker1_RangCafe", "fullName": "Worker1_RangCafe", "jobLabels": ["Rang xay", "sản xuất"]},
        {"userId": "w2", "username": "cuong", "fullName": "cuong", "jobLabels": ["Đóng gói", "tem nhan"]},
        {"userId": "w3", "username": "Ban_QC", "fullName": "Bạn QC", "jobLabels": ["kiem tra", "do am"]},
    ]
    payload = {
        "teamId": "demo-team",
        "intent": "PRODUCTION_PLAN",
        "fields": {
            "title": "Gia công 200kg cà phê Arabica",
            "productName": "Arabica",
            "quantity": 200,
            "unit": "kg",
            "deadline": "2026-08-04T17:00:00",
        },
        "members": members,
    }
    status, res = request_json("POST", "/plan", payload)
    print_json("TEST CASE 1: SEMANTIC MATCH ACROSS 3 ROLES", {"status": status, "response": res})
    assert_true(status == 200, "Case 1 should return 200")
    tasks = res.get("tasks", [])
    assert_true(len(tasks) >= 3, "Case 1 should generate at least 3 tasks")

    # Verify roasting task assigned to w1
    rang_task = next((t for t in tasks if "rang" in t["title"].lower()), None)
    assert_true(rang_task is not None, "Case 1 must have a roasting task")
    assert_true(rang_task.get("suggestedAssigneeId") == "w1", f"Roasting task should be assigned to w1, got: {rang_task.get('suggestedAssigneeId')}")

    # Verify packaging task assigned to w2
    pack_task = next((t for t in tasks if "đóng gói" in t["title"].lower() or "bao bì" in t["title"].lower()), None)
    if pack_task:
        assert_true(pack_task.get("suggestedAssigneeId") == "w2", f"Packaging task should be assigned to w2, got: {pack_task.get('suggestedAssigneeId')}")


def test_case_2_anti_hallucination_null() -> None:
    members = [
        {"userId": "w1", "username": "Worker1_RangCafe", "fullName": "Worker1_RangCafe", "jobLabels": ["Rang xay"]},
        {"userId": "w2", "username": "cuong", "fullName": "cuong", "jobLabels": ["Đóng gói"]},
    ]
    payload = {
        "teamId": "demo-team",
        "intent": "OPERATION_TASK",
        "fields": {
            "title": "Vệ sinh bảo dưỡng máy rang và thử nếm mẻ cà phê",
            "deadline": "2026-08-04T17:00:00",
        },
        "members": members,
    }
    status, res = request_json("POST", "/plan", payload)
    print_json("TEST CASE 2: ANTI-HALLUCINATION NULL ASSIGNEE", {"status": status, "response": res})
    assert_true(status == 200, "Case 2 should return 200")
    tasks = res.get("tasks", [])
    # Verify no fake assignees for un-matched cleaning/maintenance
    for t in tasks:
        if "vệ sinh" in t["title"].lower() or "bảo dưỡng" in t["title"].lower():
            assert_true(t.get("suggestedAssigneeId") is None, "Cleaning task must be null when no cleaning label exists")


def test_case_3_multi_skill_match() -> None:
    members = [
        {"userId": "m1", "username": "Worker_Versatile", "fullName": "Worker_Versatile", "jobLabels": ["Phối trộn", "Medium Roast", "rang", "san xuat", "Đóng gói"]},
        {"userId": "m2", "username": "Worker_Cleaner", "fullName": "Worker_Cleaner", "jobLabels": ["Chỉ quét dọn"]},
    ]
    payload = {
        "teamId": "demo-team",
        "intent": "PRODUCTION_PLAN",
        "fields": {
            "title": "Phối trộn 70% Robusta 30% Arabica sau đó rang Medium Roast",
            "productName": "Blend Robusta Arabica",
            "quantity": 100,
            "unit": "kg",
            "deadline": "2026-08-04T17:00:00",
        },
        "members": members,
    }
    status, res = request_json("POST", "/plan", payload)
    print_json("TEST CASE 3: MULTI-SKILL MATCHING", {"status": status, "response": res})
    assert_true(status == 200, "Case 3 should return 200")
    tasks = res.get("tasks", [])
    # Verify versatile worker is suggested for blending, roasting, and packaging, but NOT for QC
    for t in tasks:
        title_lower = t["title"].lower()
        if "qc" in title_lower or "kiểm tra" in title_lower:
            assert_true(t.get("suggestedAssigneeId") is None, f"QC task should be null, got: {t.get('suggestedAssigneeId')}")
        elif any(k in title_lower for k in ["phối trộn", "rang", "đóng gói"]):
            assert_true(t.get("suggestedAssigneeId") == "m1", f"Task {t['title']} should be assigned to m1, got: {t.get('suggestedAssigneeId')}")


def test_case_4_dynamic_revise_assignee() -> None:
    members = [
        {"userId": "w1", "username": "Worker1_RangCafe", "fullName": "Worker1_RangCafe", "jobLabels": ["Rang xay"]},
        {"userId": "u2", "username": "Cuongpro", "fullName": "Cuongpro", "jobLabels": ["Quản lý"]},
    ]
    initial_draft = {
        "goalTitle": "Sản xuất 100kg Arabica",
        "outputTarget": "100kg Arabica thành phẩm",
        "deadline": "2026-08-04T17:00:00",
        "priority": 3,
        "tasks": [
            {
                "title": "Rang 100kg cà phê Arabica",
                "description": "Thực hiện rang mẻ cà phê Arabica.",
                "priority": 4,
                "workload": 4.0,
                "suggestedAssigneeId": "w1",
                "suggestedAssigneeName": "Worker1_RangCafe",
                "suggestedReason": "Phù hợp nhãn rang xay.",
            }
        ],
    }
    payload = {
        "teamId": "demo-team",
        "instruction": "Đổi task rang cho Cuongpro làm giúp tôi",
        "draft": initial_draft,
        "members": members,
    }
    status, res = request_json("POST", "/revise", payload)
    print_json("TEST CASE 4: DYNAMIC REVISE ASSIGNEE", {"status": status, "response": res})
    assert_true(status == 200, "Case 4 should return 200")
    tasks = res.get("tasks", [])
    assert_true(len(tasks) > 0, "Case 4 should return tasks")
    rang_task = tasks[0]
    assert_true(rang_task.get("suggestedAssigneeId") == "u2", f"Revised task should be assigned to Cuongpro (u2), got: {rang_task.get('suggestedAssigneeId')}")


def test_case_5_empty_joblabels_exclusion() -> None:
    members = [
        {"userId": "empty_u", "username": "UserA", "fullName": "UserA", "jobLabels": []},
        {"userId": "xay_u", "username": "UserB", "fullName": "UserB", "jobLabels": ["xay pha phin", "micron"]},
    ]
    payload = {
        "teamId": "demo-team",
        "intent": "PRODUCTION_PLAN",
        "fields": {
            "title": "Xay 50kg cà phê pha phin hạt mịn 600 micron",
            "productName": "Cà phê xay",
            "quantity": 50,
            "unit": "kg",
            "deadline": "2026-08-04T17:00:00",
        },
        "members": members,
    }
    status, res = request_json("POST", "/plan", payload)
    print_json("TEST CASE 5: EMPTY JOBLABELS EXCLUSION", {"status": status, "response": res})
    assert_true(status == 200, "Case 5 should return 200")
    tasks = res.get("tasks", [])
    xay_task = next((t for t in tasks if "xay" in t["title"].lower()), None)
    assert_true(xay_task is not None, "Case 5 must have a grinding task")
    assert_true(xay_task.get("suggestedAssigneeId") == "xay_u", f"Grinding task should be assigned to UserB (xay_u), got: {xay_task.get('suggestedAssigneeId')}")


def main() -> int:
    health_status, health = request_json("GET", "/health")
    print_json("HEALTH CHECK", {"status": health_status, "body": health})
    assert_true(health_status == 200, "AI Service must be running")

    test_case_1_semantic_match()
    test_case_2_anti_hallucination_null()
    test_case_3_multi_skill_match()
    test_case_4_dynamic_revise_assignee()
    test_case_5_empty_joblabels_exclusion()

    print("\nALL 5 HARD ASSIGNEE TEST CASES PASSED SUCCESSFULLY!")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"\nRESULT=FAIL {exc}")
        raise SystemExit(1)
