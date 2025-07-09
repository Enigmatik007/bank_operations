"""Главный модуль для взаимодействия с пользователем и обработки транзакций."""

from functools import lru_cache
from typing import Any, Dict, List, Optional

from src.decorators import log
from src.external_api import convert_to_rub
from src.processing import filter_by_state, search_by_description, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


@log(filename='logs/main.log')
def main() -> None:
    """Основная функция программы для работы с банковскими транзакциями."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        print("0. Выход")

        choice = input("> ").strip()

        if choice == '0':
            print("До свидания!")
            break

        file_type_map = {
            '1': 'json',
            '2': 'csv',
            '3': 'xlsx'
        }

        file_type = file_type_map.get(choice)
        if file_type is None:
            print("Неверный выбор. Пожалуйста, введите число от 0 до 3.")
            continue

        print(f"\nДля обработки выбран {file_type.upper()}-файл.")
        transactions = _load_data(file_type)

        if not transactions:
            print("Не удалось загрузить транзакции. Файл пуст или имеет неверный формат.")
            continue

        filtered_transactions = _filter_by_user_input(transactions)
        if not filtered_transactions:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
            continue

        sorted_transactions = _sort_by_user_input(filtered_transactions)
        rub_only = _ask_yes_no("Выводить только рублевые транзакции? Да/Нет")

        if rub_only:
            sorted_transactions = [t for t in sorted_transactions
                                 if t.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB']

        if _ask_yes_no("Отфильтровать список транзакций по определенному слову в описании? Да/Нет"):
            search_word = input("Введите слово для поиска в описании: ").strip()
            if search_word:
                sorted_transactions = search_by_description(sorted_transactions, search_word)

        _print_transactions(sorted_transactions)


@lru_cache(maxsize=3)
def _load_data(file_type: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из файла с кешированием."""
    file_map = {
        'json': 'operations.json',           # или 'transactions.json', если у вас так
        'csv': 'transactions.csv',
        'xlsx': 'transactions_excel.xlsx',
    }
    file_name = file_map.get(file_type)
    if not file_name:
        print(f"Неизвестный тип файла: {file_type}")
        return []
    file_path = f"data/{file_name}"
    return load_transactions(file_path)


def _filter_by_user_input(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Фильтрует транзакции по статусу, введенному пользователем."""
    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input("> ").strip().upper()

        if status in ('EXECUTED', 'CANCELED', 'PENDING'):
            filtered = filter_by_state(transactions, status)
            print(f"\nОперации отфильтрованы по статусу '{status}'")
            return filtered
        else:
            print(f"\nСтатус операции '{status}' недоступен.")


def _sort_by_user_input(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Сортирует транзакции по дате согласно выбору пользователя."""
    if not _ask_yes_no("Отсортировать операции по дате? Да/Нет"):
        return transactions

    while True:
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        if order in ('по возрастанию', 'возрастанию', 'возрастание'):
            return sort_by_date(transactions, reverse=False)
        elif order in ('по убыванию', 'убыванию', 'убывание'):
            return sort_by_date(transactions, reverse=True)
        else:
            print("Пожалуйста, введите 'по возрастанию' или 'по убыванию'")


def _ask_yes_no(question: str) -> bool:
    """Задает пользователю вопрос с ответом Да/Нет."""
    while True:
        answer = input(f"{question} ").strip().lower()
        if answer in ('да', 'д', 'yes', 'y'):
            return True
        elif answer in ('нет', 'н', 'no', 'n'):
            return False
        else:
            print("Пожалуйста, ответьте 'Да' или 'Нет'")


def _print_transactions(transactions: List[Dict[str, Any]]) -> None:
    """Выводит отформатированный список транзакций."""
    print("\nРаспечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")

    for transaction in transactions:
        date = get_date(transaction['date']) if 'date' in transaction else 'Нет даты'
        description = transaction.get('description', 'Без описания')

        # Обработка отправителя и получателя
        from_info = mask_account_card(transaction.get('from', '')) if transaction.get('from') else ''
        to_info = mask_account_card(transaction.get('to', '')) if transaction.get('to') else ''

        # Обработка суммы
        amount_info = transaction.get('operationAmount', {})
        amount = float(amount_info.get('amount', 0)) if amount_info.get('amount') else 0
        currency = amount_info.get('currency', {}).get('code', '')

        if currency and currency != 'RUB':
            amount_rub = convert_to_rub(transaction)
            amount_str = f"{amount} {currency} (~{amount_rub:.2f} руб.)" if amount_rub else f"{amount} {currency}"
        else:
            amount_str = f"{amount} руб."

        # Вывод информации о транзакции
        print(f"{date} {description}")
        if from_info and to_info:
            print(f"{from_info} -> {to_info}")
        elif from_info:
            print(f"{from_info}")
        elif to_info:
            print(f"{to_info}")
        print(f"Сумма: {amount_str}\n")


if __name__ == '__main__':
    main()
