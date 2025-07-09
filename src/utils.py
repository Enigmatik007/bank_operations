"""Модуль для загрузки банковских транзакций из файлов различных форматов."""

import csv
import json
from pathlib import Path
from typing import Any, Dict, List, Union

import pandas as pd

from .decorators import log


@log(filename='logs/utils.log')
def load_transactions(file_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """Загружает список транзакций из файла указанного формата."""
    try:
        path = Path(file_path)
        if path.suffix == '.json':
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        elif path.suffix == '.csv':
            with open(path, 'r', encoding='utf-8') as f:
                return [dict(row) for row in csv.DictReader(f)]  # Явное преобразование
        elif path.suffix == '.xlsx':
            df = pd.read_excel(path, engine='openpyxl')
            return [dict(row) for row in df.to_dict('records')]  # Явное преобразование
        else:
            raise ValueError(f"Неизвестный формат файла: {path.suffix}")
    except Exception:
        return []
