"""Модуль для обработки банковских транзакций: фильтрация, сортировка, поиск и анализ."""
from typing import List, Dict
from functools import lru_cache
import re
from src.decorators import log

### --- Фильтрация и сортировка транзакций ---
def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Возвращает транзакции с указанным статусом (например, 'EXECUTED').

    Args:
        operations: Список транзакций.
        state: Статус для фильтрации (по умолчанию "EXECUTED").

    Returns:
        Отфильтрованный список операций.
    """
    return [op for op in operations if op.get("state") == state]

def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортирует транзакции по дате (новые сверху по умолчанию).

    Args:
        operations: Список операций с полем "date".
        reverse: Сортировка по убыванию (по умолчанию True).

    Returns:
        Отсортированный список операций.
    """
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)

### --- Поиск и анализ транзакций ---
@log(filename='logs/processing.log')
def search_by_description(transactions: List[Dict], search_str: str) -> List[Dict]:
    """Ищет транзакции, содержащие указанную строку в описании (регистронезависимо).

    Args:
        transactions: Список транзакций.
        search_str: Строка для поиска (например, 'перевод').

    Returns:
        Список транзакций, где description содержит search_str.
    Raises:
        ValueError: Если поиск не удался.
    """
    try:
        pattern = re.compile(re.escape(search_str), re.IGNORECASE)
        return [t for t in transactions if pattern.search(t.get('description', ''))]
    except Exception as e:
        raise ValueError(f"Ошибка поиска: {e}")

@log()
@lru_cache(maxsize=100)
def count_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает, сколько раз встречается каждая категория операций.

    Args:
        transactions: Список транзакций.
        categories: Список категорий для подсчёта (например, ['Перевод', 'Оплата']).

    Returns:
        Словарь вида {'категория': количество}.
    """
    if not transactions or not categories:
        return {}
    descriptions = [t.get('description', '') for t in transactions]
    return {cat: descriptions.count(cat) for cat in categories if cat in descriptions}
