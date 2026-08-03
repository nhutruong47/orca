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


def test_tc08_vague_input() -> None:
    payload = {"teamId": "demo-team", "text": "Làm cái kia cho khách"}
    status, res = request_json("POST", "/extract", payload)
    print_json("TC08 - VAGUE INPUT (Làm cái kia cho khách)", {"status": status, "response": res})
    assert_true(status == 200, "TC08 should return 200")
    assert_true(res.get("intent") == "UNKNOWN", "TC08 intent should be UNKNOWN")
    assert_true("taskDescription" in res.get("missingFields", []), "TC08 should miss taskDescription")
    assert_true(bool(res.get("clarifyingQuestion")), "TC08 should provide clarifyingQuestion")


def test_tc10_unsupported_summary() -> None:
    payload = {"teamId": "demo-team", "text": "Tóm tắt tiến độ xưởng hôm nay"}
    status, res = request_json("POST", "/extract", payload)
    print_json("TC10 - UNSUPPORTED SUMMARY (Tóm tắt tiến độ xưởng)", {"status": status, "response": res})
    assert_true(status == 200, "TC10 should return 200")
    assert_true(res.get("intent") == "UNKNOWN", "TC10 intent should be UNKNOWN")
    assert_true(bool(res.get("clarifyingQuestion")), "TC10 should provide clarifyingQuestion")


def test_tc18_financial_query() -> None:
    payload = {"teamId": "demo-team", "text": "Báo cáo doanh thu tháng này"}
    status, res = request_json("POST", "/extract", payload)
    print_json("TC18 - FINANCIAL QUERY (Báo cáo doanh thu)", {"status": status, "response": res})
    assert_true(status == 200, "TC18 should return 200")
    assert_true(res.get("intent") == "UNKNOWN", "TC18 intent should be UNKNOWN")
    assert_true(bool(res.get("clarifyingQuestion")), "TC18 should provide clarifyingQuestion")


def test_tc19_general_weather_query() -> None:
    payload = {"teamId": "demo-team", "text": "Dự báo thời tiết mai thế nào"}
    status, res = request_json("POST", "/extract", payload)
    print_json("TC19 - GENERAL OUT-OF-SCOPE (Dự báo thời tiết)", {"status": status, "response": res})
    assert_true(status == 200, "TC19 should return 200")
    assert_true(res.get("intent") == "UNKNOWN", "TC19 intent should be UNKNOWN")
    assert_true(bool(res.get("clarifyingQuestion")), "TC19 should provide clarifyingQuestion")


def main() -> int:
    health_status, health = request_json("GET", "/health")
    print_json("HEALTH CHECK", {"status": health_status, "body": health})
    assert_true(health_status == 200, "AI Service must be running")

    test_tc08_vague_input()
    test_tc10_unsupported_summary()
    test_tc18_financial_query()
    test_tc19_general_weather_query()

    print("\nALL OUT-OF-SCOPE TEST CASES PASSED SUCCESSFULLY!")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"\nRESULT=FAIL {exc}")
        raise SystemExit(1)
