"""
Автопроверка домашнего задания занятия 03.
Запуск:  python -m pytest -v
Этот файл менять НЕЛЬЗЯ — он и есть техническое задание.
"""
import pytest

from homework import filter_by_period, find_duplicates, monthly_summary

OPS = [
    {"date": "2026-08-01", "description": "Пятёрочка", "category": "Продукты", "amount": -124550},
    {"date": "2026-08-03", "description": "Кофейня", "category": "Кафе", "amount": -32000},
    {"date": "2026-08-03", "description": "Кофейня", "category": "Кафе", "amount": -32000},
    {"date": "2026-08-05", "description": "Зарплата", "category": "Доход", "amount": 8750000},
    {"date": "2026-09-02", "description": "Метро", "category": "Транспорт", "amount": -7000},
    {"date": "2026-09-02", "description": "Метро", "category": "Транспорт", "amount": -7000},
]


# ---------- Задание 1: filter_by_period ----------
def test_filter_period_middle():
    got = filter_by_period(OPS, "2026-08-03", "2026-08-05")
    assert [op["description"] for op in got] == ["Кофейня", "Кофейня", "Зарплата"]


def test_filter_period_includes_borders():
    got = filter_by_period(OPS, "2026-08-01", "2026-08-01")
    assert len(got) == 1 and got[0]["description"] == "Пятёрочка"


def test_filter_period_keeps_order():
    got = filter_by_period(OPS, "2026-08-01", "2026-09-02")
    assert got == OPS


def test_filter_period_empty_result():
    assert filter_by_period(OPS, "2026-10-01", "2026-10-31") == []


def test_filter_period_does_not_change_input():
    before = len(OPS)
    filter_by_period(OPS, "2026-08-01", "2026-08-02")
    assert len(OPS) == before


def test_filter_period_returns_new_list():
    got = filter_by_period(OPS, "2026-08-01", "2026-09-02")
    assert got is not OPS


# ---------- Задание 2: find_duplicates ----------
def test_find_duplicates_count():
    assert len(find_duplicates(OPS)) == 2


def test_find_duplicates_order():
    got = find_duplicates(OPS)
    assert [op["description"] for op in got] == ["Кофейня", "Метро"]


def test_find_duplicates_none():
    ops = [
        {"date": "2026-08-01", "description": "A", "amount": -100},
        {"date": "2026-08-02", "description": "A", "amount": -100},
    ]
    assert find_duplicates(ops) == []


def test_find_duplicates_different_amount_is_not_duplicate():
    ops = [
        {"date": "2026-08-01", "description": "A", "amount": -100},
        {"date": "2026-08-01", "description": "A", "amount": -200},
    ]
    assert find_duplicates(ops) == []


def test_find_duplicates_triple_counts_once():
    ops = [{"date": "2026-08-01", "description": "A", "amount": -100}] * 3
    assert len(find_duplicates(ops)) == 1


def test_find_duplicates_empty():
    assert find_duplicates([]) == []


# ---------- Задание 3: monthly_summary ----------
def test_monthly_summary_months():
    assert sorted(monthly_summary(OPS)) == ["2026-08", "2026-09"]


def test_monthly_summary_august():
    assert monthly_summary(OPS)["2026-08"] == {"income": 8750000, "expense": 188550}


def test_monthly_summary_september():
    assert monthly_summary(OPS)["2026-09"] == {"income": 0, "expense": 14000}


def test_monthly_summary_expense_is_positive():
    for month in monthly_summary(OPS).values():
        assert month["expense"] >= 0


def test_monthly_summary_has_both_keys():
    got = monthly_summary([{"date": "2026-08-01", "amount": -100}])
    assert got["2026-08"] == {"income": 0, "expense": 100}


def test_monthly_summary_empty():
    assert monthly_summary([]) == {}
