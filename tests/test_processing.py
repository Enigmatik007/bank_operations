"""Оптимальные тесты для processing.py с параметризацией ключевых функций."""

from typing import Any, Dict, List

import pytest

from src.processing import count_by_category, filter_by_state, search_by_description, sort_by_date


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    """Фикстура с тестовыми транзакциями.

    Returns:
        List[Dict]: Список тестовых транзакций.
    """
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01", "description": "Перевод организации"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-02", "description": "Оплата услуг"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03", "description": "Перевод физлицу"},
        {"id": 4, "state": "PENDING", "date": "2023-01-04", "description": "Оплата налогов"},
    ]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2]),
        ("PENDING", [4]),
        ("UNKNOWN", []),
    ],
    ids=["executed", "canceled", "pending", "unknown"],
)
def test_filter_by_state(sample_data: List[Dict[str, Any]], state: str, expected_ids: List[int]) -> None:
    """Проверяет фильтрацию по разным статусам.

    Args:
        sample_data: Тестовые данные транзакций.
        state: Статус для фильтрации.
        expected_ids: Ожидаемые ID транзакций после фильтрации.
    """
    result = filter_by_state(sample_data, state)
    assert [t["id"] for t in result] == expected_ids


@pytest.mark.parametrize(
    "reverse, expected_first_id",
    [
        (True, 4),
        (False, 1),
    ],
    ids=["descending", "ascending"],
)
def test_sort_by_date(sample_data: List[Dict[str, Any]], reverse: bool, expected_first_id: int) -> None:
    """Проверяет сортировку в разных направлениях.

    Args:
        sample_data: Тестовые данные транзакций.
        reverse: Направление сортировки.
        expected_first_id: Ожидаемый ID первой транзакции после сортировки.
    """
    result = sort_by_date(sample_data, reverse)
    assert result[0]["id"] == expected_first_id


@pytest.mark.parametrize(
    "search_str, expected_ids",
    [
        ("перевод", [1, 3]),
        ("ОПЛАТА", [2, 4]),
        ("налогов", [4]),
        ("кредит", []),
    ],
    ids=["перевод", "оплата", "налогов", "нет_совпадений"],
)
def test_search_by_description(sample_data: List[Dict[str, Any]], search_str: str, expected_ids: List[int]) -> None:
    """Проверяет поиск по описанию с разными строками.

    Args:
        sample_data: Тестовые данные транзакций.
        search_str: Строка для поиска.
        expected_ids: Ожидаемые ID транзакций после поиска.
    """
    result = search_by_description(sample_data, search_str)
    assert [t["id"] for t in result] == expected_ids


@pytest.mark.parametrize(
    "categories, expected_counts",
    [
        (["Перевод организации", "Оплата услуг"], {"Перевод организации": 1, "Оплата услуг": 1}),
        (["Перевод физлицу"], {"Перевод физлицу": 1}),
        ([], {}),
        (["Несуществующая"], {}),
    ],
    ids=["basic", "single", "empty", "unknown"],
)
def test_count_by_category(
    sample_data: List[Dict[str, Any]], categories: List[str], expected_counts: Dict[str, int]
) -> None:
    """Проверяет подсчёт операций для разных наборов категорий.

    Args:
        sample_data: Тестовые данные транзакций.
        categories: Список категорий для подсчёта.
        expected_counts: Ожидаемое количество операций по категориям.
    """
    result = count_by_category(sample_data, categories)
    assert result == expected_counts
