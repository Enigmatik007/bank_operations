"""Конфигурация тестов и фикстур для банковских операций."""

from typing import Any, Dict, List, Tuple

import pytest


@pytest.fixture
def sample_operations() -> List[Dict[str, Any]]:
    """
    Фикстура предоставляет тестовые данные банковских операций.

    Returns:
        List[Dict]: Список операций с разными статусами и датами.
    """
    return [
        {"state": "EXECUTED", "date": "2024-03-11T02:26:18.671407", "description": "Перевод организации"},
        {"state": "PENDING", "date": "2023-12-31T23:59:59.999999", "description": "Перевод с карты на карту"},
    ]


@pytest.fixture
def card_and_account_data() -> List[Tuple[str, str]]:
    """
    Фикстура для тестовых данных карт и счетов.

    Returns:
        List[Tuple]: Пары (входные данные, ожидаемый результат).
    """
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ]
