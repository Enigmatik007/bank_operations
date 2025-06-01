from typing import List, Dict, Any


def filter_by_state(
    operations: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по указанному состоянию.

    Args:
        operations: Список словарей с банковскими операциями
        state: Состояние для фильтрации (по умолчанию 'EXECUTED')

    Returns:
        Отфильтрованный список операций с указанным состоянием
    """
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(
    operations: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате.

    Args:
        operations: Список словарей с банковскими операциями
        reverse: Порядок сортировки (True - по убыванию, False - по возрастанию)

    Returns:
        Отсортированный по дате список операций
    """
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)