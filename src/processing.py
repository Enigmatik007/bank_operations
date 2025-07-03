"""Модуль для обработки и фильтрации банковских транзакций."""


def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует операции по указанному статусу.

    Args:
        operations: Список операций.
        state: Статус для фильтрации (по умолчанию "EXECUTED").

    Returns:
        Отфильтрованный список операций.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует операции по дате.

    Args:
        operations: Список операций с полем "date".
        reverse: Флаг сортировки по убыванию (по умолчанию True).

    Returns:
        Отсортированный список операций.
    """
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)
