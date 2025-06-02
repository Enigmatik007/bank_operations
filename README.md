Вот отформатированная и структурированная версия README с улучшенной читаемостью и правильным markdown-разметкой:

```markdown
# Банковские операции — Модуль маскировки данных

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)  
[![Poetry](https://img.shields.io/badge/Poetry-1.8+-orange.svg)](https://python-poetry.org)  
[![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen.svg)](#)

Модуль для обработки и маскировки банковских данных с полным покрытием тестами.

---

## 📦 Установка

1. Клонируйте репозиторий:
   ```powershell
   git clone https://github.com/Enigmatik007/bank_operations
   cd bank_operations
   ```

2. Установите зависимости через Poetry:
   ```bash
   poetry install
   ```

---

## 🛠️ Функционал

### 🔐 Маскировка данных

| Модуль      | Функция                  | Пример ввода → Вывода                           |
|-------------|--------------------------|-------------------------------------------------|
| `masks.py`  | `get_mask_card_number()` | `"7000792289606361"` → `"7000 79** **** 6361"`  |
|             | `get_mask_account()`     | `"73654108430135874305"` → `"**4305"`           |
| `widget.py` | `mask_account_card()`    | `"Visa 7000..."` → `"Visa 7000 79** **** 6361"` |
|             | `get_date()`             | `"2024-03-11T02:..."` → `"11.03.2024"`          |

### 🔍 Обработка операций

```python
from src.processing import filter_by_state, sort_by_date

# Фильтрация по статусу
filtered = filter_by_state(operations, "EXECUTED")

# Сортировка по дате
sorted_ops = sort_by_date(operations)
```

---

## 🧪 Тестирование

Запуск всех тестов с проверкой покрытия:

```bash
poetry run pytest --cov=src --cov-report=html
```

Структура тестов:

```
tests/
├── test_masks.py        # Тесты масок (7 параметризованных тестов)
├── test_processing.py   # Тесты обработки (2 фикстуры)
└── test_widget.py       # Тесты виджетов (4 параметризованных теста)
```

---

## 📊 Отчет о покрытии

После запуска тестов откройте отчет:

```bash
start htmlcov/index.html
```

---

## 🚀 Использование

Запуск интерактивного режима:

```bash
poetry run python main.py
```

Пример работы:

```
Введите номер карты (16 цифр): 7000792289606361
Маска карты: 7000 79** **** 6361

Введите 'Тип Номер': Счет 73654108430135874305
Результат: Счет **4305
```

---

## ✅ Контроль качества

Статический анализ:

```bash
poetry run flake8 .
poetry run mypy .
```

Форматирование кода:

```bash
poetry run autopep8 --in-place --aggressive src/
```

---

## 📌 Особенности

- Полная типизация (mypy)
- 100% покрытие тестами
- Параметризованные тесты
- Интеграция с Poetry

---

## 📝 Лицензия

MIT © 2024 Данилов Евгений Сергеевич

```

