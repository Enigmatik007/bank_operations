from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> filter:
    """
    Фильтрует транзакции по заданной валюте.

    Args:
        transactions: Список словарей с транзакциями
        currency: Код валюты (например, "USD")

    Returns:
        Итератор, возвращающий только транзакции в указанной валюте
    """
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)


def transaction_descriptions(transactions: list[dict]) -> map:
    """
    Генерирует описания транзакций.

    Args:
        transactions: Список словарей с транзакциями

    Yields:
        Описание каждой транзакции
    """
    return map(lambda x: x["description"], transactions)


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генерирует номера карт в заданном диапазоне.

    Args:
        start: Начальный номер
        end: Конечный номер

    Yields:
        Номера карт в формате "XXXX XXXX XXXX XXXX"
    """
    for num in range(start, end + 1):
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:16]
