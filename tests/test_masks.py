import pytest
from src.masks import get_mask_card_number, get_mask_account


# Тесты для валидных данных
@pytest.mark.parametrize("card_num, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("5555444433332222", "5555 44** **** 2222")
])
def test_get_mask_card_number_valid(card_num, expected):
    assert get_mask_card_number(card_num) == expected


@pytest.mark.parametrize("account_num, expected", [
    ("123456789012", "**9012"),
    ("987654321098", "**1098")
])
def test_get_mask_account_valid(account_num, expected):
    assert get_mask_account(account_num) == expected


# Тесты для невалидных данных
def test_get_mask_card_number_invalid():
    with pytest.raises(ValueError):
        get_mask_card_number("123")  # Слишком короткий

    with pytest.raises(ValueError):
        get_mask_card_number("abcdefghijklmnop")  # Не цифры


def test_get_mask_account_invalid():
    with pytest.raises(ValueError):
        get_mask_account("123")  # Меньше 4 цифр

    with pytest.raises(ValueError):
        get_mask_account("abcd")  # Буквы вместо цифр