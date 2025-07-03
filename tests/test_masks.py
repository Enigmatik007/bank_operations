"""Тесты для модуля masks.py.

Проверяют корректность валидации и маскирования реквизитов.
"""

import pytest
from src.masks import _validate_number, get_mask_account, get_mask_card_number

@pytest.mark.parametrize(
    "card_num, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456")
    ],
    ids=["visa", "mastercard"]
)
def test_get_mask_card_number_valid(card_num: str, expected: str) -> None:
    """Тестирует корректное маскирование валидных номеров карт."""
    assert get_mask_card_number(card_num) == expected

@pytest.mark.parametrize(
    "account_num, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345678", "**5678")
    ],
    ids=["long_account", "short_account"]
)
def test_get_mask_account_valid(account_num: str, expected: str) -> None:
    """Тестирует корректное маскирование валидных номеров счетов."""
    assert get_mask_account(account_num) == expected

@pytest.mark.parametrize(
    "number, length, name, expected_msg",
    [
        ("123", 4, "карты", "Номер карты должен содержать минимум 4 цифр"),
        ("abcd", 4, "счета", "Номер счета должен содержать только цифры"),
        ("", 4, "карты", "Номер карты должен содержать только цифры"),
        ("12345a", 10, "счета", "Номер счета должен содержать только цифры")
    ],
    ids=["short_num", "non_digit", "empty", "mixed_chars"]
)
def test_validate_number_errors(number: str, length: int, name: str, expected_msg: str) -> None:
    """Тестирует обработку ошибок валидации."""
    with pytest.raises(ValueError) as exc_info:
        _validate_number(number, length, name)
    assert str(exc_info.value) == expected_msg
