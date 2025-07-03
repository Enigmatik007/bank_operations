<p align="center">
  <img src="https://img.icons8.com/clouds/500/bank-card-back-side.png" alt="bank operations logo" width="160"/>
</p>

<h1 align="center">💳 Банковские операции</h1>

<p align="center">
  <strong>Полный набор инструментов для работы с банковскими транзакциями</strong><br>
  <em>Генерация, маскировка, конвертация и анализ с 100% покрытием тестами</em>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12+-blue.svg" alt="Python"></a>
  <a href="https://python-poetry.org/"><img src="https://img.shields.io/badge/Poetry-1.8+-orange.svg" alt="Poetry"></a>
  <img src="https://img.shields.io/badge/Coverage-100%25-brightgreen.svg" alt="Coverage">
</p>

---

## 📦 Установка

```bash
git clone https://github.com/Enigmatik007/bank_operations
cd bank_operations
poetry install
```

---

## 🧰 Функциональные модули

### 🔍 `generators.py` — генераторы данных

- `filter_by_currency(transactions, currency)` — фильтрует транзакции по валюте.
- `transaction_descriptions(transactions)` — описания транзакций.
- `card_number_generator(start, end)` — генератор номеров карт в формате `XXXX XXXX XXXX XXXX`.

### 🔐 `masks.py` — маскировка данных

- `get_mask_card_number(card_number)` — маскирует номер карты: `7000 79** **** 6361`.
- `get_mask_account(account_number)` — маскирует счёт: `**4305`.

### 🧮 `processing.py` — логика обработки

- `filter_by_state(operations, state)` — фильтрация по статусу (`EXECUTED`, `PENDING` и т.д.).
- `sort_by_date(operations, reverse=True)` — сортировка по дате.

### 🧱 `widget.py` — вспомогательные функции

- `mask_account_card(data)` — автоматическая маскировка карты или счёта.
- `get_date(date_str)` — преобразует дату из ISO в формат `ДД.ММ.ГГГГ`.


### 📊 Загрузка данных (utils.py)

```python
  
def load_transactions(file_path: str) -> list[dict]  # Загрузка JSON-файла

```

### 🌐 Внешние API (external_api.py)

```python
  
def convert_to_rub(transaction: dict) -> float | None  # Конвертация в RUB через API

```

### 📝 Логирование (decorators.py)

- `@log(filename=None)` — декоратор для логирования вызовов функций:
  - Логирование в файл при указании `filename`
  - Вывод в консоль, если `filename` не указан
  - Фиксация времени, параметров и результатов вызовов
  - Запись ошибок с сохранением входных параметров
---

## 🚀 Примеры использования

```python
from src.generators import filter_by_currency, card_number_generator
from src.widget import mask_account_card, get_date

usd_ops = filter_by_currency(transactions, "USD")
print(next(usd_ops))

for num in card_number_generator(1, 3):
    print(num)  # 0000 0000 0000 0001 ...

print(mask_account_card("Visa 7000792289606361"))  # Visa 7000 79** **** 6361
print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
```

---

## 🧪 Тестирование (100%)

Запуск тестов и генерация отчёта покрытия:

```bash
poetry run pytest --cov=src --cov-report=html
start htmlcov/index.html  # открыть отчет в браузере (Windows)
```

### Структура тестов

```
tests/
├── __init__.py             # Инициализация тестового пакета
├── conftest.py             # Общие фикстуры:
│                           # - sample_transactions
│                           # - card_and_account_data
│                           # - mock_api
├── test_decorators.py      # Тесты декоратора @log
├── test_external_api.py    # Тесты работы с внешним API
├── test_generators.py      # Тесты генераторов транзакций
├── test_masks.py           # Тесты маскировки (валидные/ошибочные случаи)
├── test_processing.py      # Тесты обработки операций
├── test_utils.py           # Тесты загрузки данных
└── test_widget.py          # Тесты виджета (маскировка + даты)
```

Все тесты покрыты параметризацией и снабжены комментариями.

---

## ✅ Контроль качества

```bash
poetry run flake8 src/
poetry run black src/
poetry run isort src/
```

---

---

## 📌 Особенности

- ✅ Поддержка Python 3.12+
- 🧠 Полная типизация и валидация
- 🌀 Использование генераторов
- 🔒 Маскировка конфиденциальных данных
- 💯 Покрытие тестами = 100%
- 🧪 Параметризованные тесты и фикстуры
- 📦 Poetry как менеджер зависимостей

---

## 📝 Лицензия

MIT © 2024 Данилов Евгений Сергеевич
