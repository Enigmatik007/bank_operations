from typing import Any, Dict, List


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по указанному статусу.

    Args:
        operations: Список операций.
        state: Статус для фильтрации (по умолчанию "EXECUTED").

    Returns:
        Список операций с указанным статусом.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует операции по дате (по убыванию по умолчанию).

    Args:
        operations: Список операций с полем "date".
        reverse: Порядок сортировки (True - по убыванию).

    Returns:
        Отсортированный список операций.
    """
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)
