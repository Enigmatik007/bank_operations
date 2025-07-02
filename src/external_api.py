import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY', 'test_key')  # Добавляем значение по умолчанию для тестов
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: Dict) -> Optional[float]:
    """
    Конвертирует сумму транзакции в рубли.
    """
    try:
        amount = float(transaction['operationAmount']['amount'])
        currency = transaction['operationAmount']['currency']['code']

        if currency == 'RUB':
            return amount

        response = requests.get(
            BASE_URL,
            params={'base': currency, 'symbols': 'RUB'},
            headers={'apikey': API_KEY},
            timeout=5
        )
        response.raise_for_status()
        rate = response.json()['rates']['RUB']
        return round(amount * rate, 2)

    except (KeyError, ValueError, TypeError, requests.RequestException):
        return None
