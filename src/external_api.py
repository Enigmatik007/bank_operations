"""Модуль для работы с внешними API банковских сервисов."""

import os
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY: Optional[str] = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL: str = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: dict) -> Optional[float]:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными о транзакции

    Returns:
        Сумма в рублях или None при ошибке
    """
    try:
        amount_str: str = transaction['operationAmount']['amount']
        amount: float = float(amount_str)
        currency: str = transaction['operationAmount']['currency']['code']

        if currency == 'RUB':
            return amount

        if not API_KEY:
            return None

        response: requests.Response = requests.get(
            BASE_URL, params={'base': currency, 'symbols': 'RUB'}, headers={'apikey': API_KEY}, timeout=5
        )
        response.raise_for_status()
        rate: float = response.json()['rates']['RUB']
        return round(amount * rate, 2)

    except (KeyError, ValueError, TypeError, requests.RequestException):
        return None
