from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """
    Фикстура с тестовыми данными транзакций.
    """
    return [
        {"description": "Перевод организации", "operationAmount": {"currency": {"code": "USD"}}},
        {"description": "Перевод со счета на счет", "operationAmount": {"currency": {"code": "RUB"}}},
        {"description": "Оплата услуг", "operationAmount": {"currency": {"code": "USD"}}},
        {"description": "Снятие наличных", "operationAmount": {"currency": {"code": "RUB"}}},
        {"description": "Пополнение счета", "operationAmount": {"currency": {"code": "USD"}}},
    ]


@pytest.mark.parametrize("currency,expected_count", [("USD", 3), ("RUB", 2), ("EUR", 0)])
def test_filter_by_currency(sample_transactions: List[Dict[str, Any]], currency: str, expected_count: int) -> None:
    """
    Тестирует фильтрацию транзакций по валюте.
    """
    filtered = list(filter_by_currency(sample_transactions, currency))
    assert len(filtered) == expected_count


def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    """
    Тестирует генерацию описаний транзакций.
    """
    descriptions = list(transaction_descriptions(sample_transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Оплата услуг",
        "Снятие наличных",
        "Пополнение счета",
    ]
    assert descriptions == expected


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9995,
            9999,
            [
                "0000 0000 0000 9995",
                "0000 0000 0000 9996",
                "0000 0000 0000 9997",
                "0000 0000 0000 9998",
                "0000 0000 0000 9999",
            ],
        ),
    ],
)
def test_card_number_generator(start: int, end: int, expected: List[str]) -> None:
    """
    Тестирует генератор номеров карт.
    """
    result = list(card_number_generator(start, end))
    assert result == expected
