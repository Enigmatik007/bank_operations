"""Модуль для обработки банковских транзакций.

Содержит функции для фильтрации, сортировки, поиска и анализа транзакций.
"""

import re
from typing import Dict, List

from src.decorators import log


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует транзакции по статусу.

    Args:
        operations: Список транзакций.
        state: Статус для фильтрации (по умолчанию "EXECUTED").

    Returns:
        Отфильтрованный список операций.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортирует транзакции по дате.

    Args:
        operations: Список операций.
        reverse: Сортировка по убыванию (по умолчанию True).

    Returns:
        Отсортированный список операций.
    """
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)


@log(filename='logs/processing.log')
def search_by_description(transactions: List[Dict], search_str: str) -> List[Dict]:
    """Ищет транзакции по подстроке в описании.

    Args:
        transactions: Список транзакций.
        search_str: Подстрока для поиска.

    Returns:
        Список найденных транзакций.
    """
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get('description', ''))]


@log()
def count_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество транзакций по категориям.

    Args:
        transactions: Список транзакций.
        categories: Список категорий для подсчета.

    Returns:
        Словарь с количеством транзакций по категориям.
    """
    if not transactions or not categories:
        return {}

    # Удаляем lru_cache и изменяем реализацию
    descriptions = [t.get('description', '') for t in transactions]
    return {cat: descriptions.count(cat) for cat in categories if cat in descriptions}
