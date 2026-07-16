"""Tests for the document quality evaluator."""
from app.rag.quality import (
    evaluate_quality,
    score_for_indexed_record,
    QualityBreakdown,
)


def test_evaluate_quality_for_rich_content():
    record = {
        "content": (
            "Cà phê Robusta 1kg tại kho HCM, tồn kho 200kg, lô sản xuất 12/2024. "
            "Đây là nguồn nguyên liệu chính cho dây chuyền rang 03 và đóng gói 04. "
            "Sản phẩm đã được QC đạt chuẩn ORCA-2024 và sẵn sàng xuất cho các đơn hàng. "
            "Lô hàng nhập từ Đắk Lắk với độ ẩm 12.5%, kích cỡ sàng 16, không lẫn tạp chất. "
            "Hạt Robusta có mùi thơm đặc trưng, vị đắng đậm, hậu vị sô-cô-la. "
            "Đề xuất dùng cho phân khúc espresso và cà phê đặc sản rang đậm. "
            "Bảo quản nơi khô ráo, tránh ánh nắng trực tiếp, nhiệt độ dưới 25°C, độ ẩm dưới 65%."
        ),
        "metadata": {
            "title": "Robusta 1kg tại HCM",
            "category": "inventory",
            "last_updated": "2026-01-15T00:00:00Z",
        },
    }
    breakdown = evaluate_quality(record, source="inventory", now_epoch=1_700_000_000)
    assert 0.0 < breakdown.overall <= 1.0
    assert breakdown.completeness > 0.6
    assert breakdown.accuracy > 0.6
    assert breakdown.relevance > 0.6


def test_evaluate_quality_penalises_thin_content():
    record = {"content": "short", "metadata": {}}
    breakdown = evaluate_quality(record, source="inventory", now_epoch=1_700_000_000)
    assert breakdown.completeness < 0.4
    assert breakdown.relevance < 0.5


def test_evaluate_quality_flags_placeholder_text():
    record = {"content": "TODO: add details", "metadata": {}}
    breakdown = evaluate_quality(record, source="faq", now_epoch=1_700_000_000)
    assert breakdown.overall == 0.0
    assert "low_value" in breakdown.reasons


def test_evaluate_quality_freshness_decays():
    record = {
        "content": "Some content " * 30,
        "metadata": {
            "last_updated": "2020-01-01T00:00:00Z",
        },
    }
    fresh_breakdown = evaluate_quality(
        {"content": record["content"], "metadata": {"last_updated": "2026-01-01T00:00:00Z"}},
        source="orders",
        now_epoch=1_700_000_000,
    )
    stale_breakdown = evaluate_quality(record, source="orders", now_epoch=1_700_000_000)
    assert fresh_breakdown.freshness > stale_breakdown.freshness


def test_score_for_indexed_record_returns_dict():
    record = {
        "content": "Some sample content " * 20,
        "metadata": {"title": "Sample", "category": "manual"},
    }
    out = score_for_indexed_record(record, source="manual")
    assert "quality_score" in out
    assert "quality_components" in out
    assert "quality_reasons" in out
    assert 0.0 <= out["quality_score"] <= 1.0
    assert set(out["quality_components"].keys()) == {
        "completeness",
        "accuracy",
        "freshness",
        "relevance",
        "overall",
    }
