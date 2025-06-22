<p align="center">
  <img src="https://img.icons8.com/clouds/500/bank-card-back-side.png" alt="bank operations logo" width="160"/>
</p>

<h1 align="center">💳 Банковские операции</h1>

<p align="center">
  <strong>Обработка, Маскировка и Генерация транзакций на Python</strong><br>
  <em>С фокусом на генераторы, тесты и контроль качества</em>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12+-blue.svg" alt="Python"></a>
  <a href="https://python-poetry.org/"><img src="https://img.shields.io/badge/Poetry-1.8+-orange.svg" alt="Poetry"></a>
  <img src="https://img.shields.io/badge/Coverage-85%25-brightgreen.svg" alt="Coverage">
  <img src="https://img.shields.io/github/actions/workflow/status/Enigmatik007/bank_operations/tests.yml?branch=main&label=CI" alt="GitHub Actions">
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

### 📝 decorators.py — система логирования

- `@log(filename=None)` — декоратор для логирования вызовов функций:
  - Логирование в файл при указании `filename`
  - Вывод в консоль, если `filename` не указан
  - Фиксация времени, параметров и результатов вызовов
  - Запись ошибок с сохранением входных парам
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

## 🧪 Тестирование

Запуск тестов и генерация отчёта покрытия:

```bash
poetry run pytest --cov=src --cov-report=html
start htmlcov/index.html  # открыть отчет в браузере (Windows)
```

### Структура тестов

```
tests/
├── test_generators.py      # генераторы (валюта, описания, номера)
├── test_masks.py           # маскировка (валидные/ошибочные случаи)
├── test_processing.py      # фильтрация и сортировка
├── test_widget.py          # форматирование даты и маскировка
├── conftest.py             # фикстуры: операции, номера
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
- 💯 Покрытие тестами > 85%
- 🧪 Параметризованные тесты и фикстуры
- 🔁 Интеграция с CI/CD через GitHub Actions
- 📦 Poetry как менеджер зависимостей

---

## 📝 Лицензия

MIT © 2024 Данилов Евгений Сергеевич