import pytest

from src.masks import _validate_number, get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_num, expected",
    [("7000792289606361", "7000 79** **** 6361"), ("1234567890123456", "1234 56** **** 3456")],
    ids=["visa", "mastercard"],
)
def test_get_mask_card_number_valid(card_num: str, expected: str) -> None:
    """
    Параметризованный тест для валидных номеров карт.

    Args:
        card_num: Тестовый номер карты
        expected: Ожидаемая маска
    """
    assert get_mask_card_number(card_num) == expected


@pytest.mark.parametrize(
    "account_num, expected",
    [("73654108430135874305", "**4305"), ("12345678", "**5678")],
    ids=["long_account", "short_account"],
)
def test_get_mask_account_valid(account_num: str, expected: str) -> None:
    """
    Параметризованный тест для валидных номеров счетов.
    """
    assert get_mask_account(account_num) == expected


@pytest.mark.parametrize(
    "number, length, name, error_msg",
    [
        ("123", 4, "карты", "минимум 4 цифр"),
        ("abcd", 4, "счета", "минимум 4 цифр"),
        ("", 4, "карты", "минимум 4 цифр"),
    ],
    ids=["short_num", "non_digit", "empty"],
)
def test_validate_number_errors(number: str, length: int, name: str, error_msg: str) -> None:
    """
    Параметризованный тест для ошибочных входных данных.
    """
    with pytest.raises(ValueError, match=error_msg):
        _validate_number(number, length, name)
