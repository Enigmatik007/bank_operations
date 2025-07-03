import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.usefixtures("card_and_account_data")
class TestWidgetFunctions:
    """Группа тестов для widget.py с использованием фикстур."""

    @pytest.mark.parametrize(
        "input_date, expected",
        [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2025-12-31T23:59:59.999999", "31.12.2025")],
        ids=["current_date", "future_date"],
    )
    def test_get_date(self, input_date: str, expected: str) -> None:
        """
        #     Параметризованный тест для форматирования даты.
        #"""
        assert get_date(input_date) == expected

    def test_mask_account_card(self, card_and_account_data: list[tuple[str, str]]) -> None:
        """
        Тест с использованием фикстуры card_and_account_data.
        """
        for input_data, expected in card_and_account_data:
            assert mask_account_card(input_data) == expected
