"""Скрипт для отладки основных функций."""

from src.masks import get_mask_account, get_mask_card_number
from src.utils import load_transactions


def test_masks() -> None:
    """Тестирование функций маскирования."""
    print('Тест масок карт:')
    print(get_mask_card_number('7000792289606361'))  # 7000 79** **** 6361
    print(get_mask_account('73654108430135874305'))  # **4305


def test_utils() -> None:
    """Тестирование загрузки транзакций."""
    print('\nТест загрузки транзакций:')
    print(load_transactions('operations.json')[:1])  # Первая операция


if __name__ == '__main__':
    test_masks()
    test_utils()
