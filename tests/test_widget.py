import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ],
)
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "input_date, expected",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2025-12-31T23:59:59.999999", "31.12.2025")],
)
def test_get_date(input_date, expected):
    assert get_date(input_date) == expected
