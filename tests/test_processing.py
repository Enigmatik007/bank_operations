"""Тесты для модуля processing."""

import pytest

from src.processing import filter_by_state, sort_by_date


class TestProcessing:
    """Тесты для processing.py с использованием фикстур."""

    def test_filter_by_state(self, sample_operations: list[dict]) -> None:
        """Тестирует фильтрацию операций по статусу."""
        filtered = filter_by_state(sample_operations, "EXECUTED")
        assert len(filtered) == 1
        assert all(op["state"] == "EXECUTED" for op in filtered)

    @pytest.mark.parametrize(
        "reverse,expected_date", [(True, "2024-03-11"), (False, "2023-12-31")], ids=["descending", "ascending"]
    )
    def test_sort_by_date(self, sample_operations: list[dict], reverse: bool, expected_date: str) -> None:
        """Тестирует сортировку операций по дате.

        Args:
            reverse: Порядок сортировки (True - по убыванию).
            expected_date: Ожидаемая дата первой операции после сортировки.
        """
        sorted_ops = sort_by_date(sample_operations, reverse)
        assert sorted_ops[0]["date"].startswith(expected_date)
