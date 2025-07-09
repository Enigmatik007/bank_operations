"""Модуль для загрузки и обработки банковских транзакций из файлов различных форматов.

Содержит функции для чтения транзакций из JSON, CSV и Excel файлов с автоматическим
определением формата и обработкой ошибок.
"""

import csv
import json
from pathlib import Path
from typing import Any, Dict, List, Union, cast

import pandas as pd
from openpyxl.utils.exceptions import InvalidFileException

from .decorators import log


@log(filename='logs/utils.log')
def load_transactions(file_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из файла указанного формата.

    Поддерживаемые форматы:
    - JSON (.json)
    - CSV (.csv)
    - Excel (.xlsx)

    Args:
        file_path (Union[str, Path]): Путь к файлу с транзакциями (строка или Path-объект).

    Returns:
        List[Dict[str, Any]]: Список словарей, где каждый словарь представляет одну транзакцию.
        В случае ошибки чтения возвращает пустой список.

    Raises:
        FileNotFoundError: Если файл не существует.
        PermissionError: Если нет прав доступа к файлу.
        ValueError: Если передан файл неподдерживаемого формата.
        json.JSONDecodeError: Для JSON файлов с синтаксическими ошибками.
        csv.Error: Для ошибок чтения CSV.
        InvalidFileException: Для битых Excel файлов.
    """
    try:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {path}")

        if path.suffix == '.json':
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    return cast(List[Dict[str, Any]], data)
                else:
                    return []
        elif path.suffix == '.csv':
            with open(path, 'r', encoding='utf-8') as f:
                rows = [dict(row) for row in csv.DictReader(f)]
                return cast(List[Dict[str, Any]], rows)
        elif path.suffix == '.xlsx':
            df = pd.read_excel(path, engine='openpyxl')
            records = df.to_dict('records')
            return [cast(Dict[str, Any], dict(row)) for row in records]
        else:
            raise ValueError(f"Неизвестный формат файла: {path.suffix}")

    except (FileNotFoundError, PermissionError):
        raise  # Пробрасываем критические ошибки доступа
    except (json.JSONDecodeError, csv.Error, InvalidFileException, ValueError) as e:
        print(f"Ошибка при обработке файла: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        raise  # Пробрасываем неожиданные исключения

