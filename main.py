"""Главный модуль для взаимодействия с пользователем и обработки транзакций."""

from functools import lru_cache
from typing import Dict, List

from src.decorators import log
from src.processing import count_by_category, filter_by_state, search_by_description, sort_by_date
from src.utils import load_transactions


@log(filename='logs/main.log')
def main() -> None:
    """Предоставляет интерфейс для работы с банковскими транзакциями."""
    print("Привет! Добро пожаловать в программу работы с транзакциями.")
    _handle_user_interaction()


def _handle_user_interaction() -> None:
    """Обрабатывает пользовательский ввод в цикле."""
    while True:
        choice = input(
            "Выберите действие:\n" "1. Загрузить транзакции\n" "2. Проанализировать данные\n" "0. Выход\n> "
        ).strip()

        if choice == '0':
            break

        if choice == '1':
            transactions = _load_data('json')  # Пример для JSON
            print(f"Загружено {len(transactions)} транзакций")
        elif choice == '2':
            print("Анализ данных...")
            # Реализация анализа


@lru_cache(maxsize=3)
def _load_data(file_type: str) -> List[Dict]:
    """Загружает транзакции из файла с кешированием."""
    file_path = f"data/transactions.{file_type}"
    return load_transactions(file_path)


if __name__ == '__main__':
    main()
