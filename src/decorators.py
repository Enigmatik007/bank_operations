"""Модуль с декоратором для логирования вызовов функций."""

import functools
import os
from datetime import datetime
from typing import Any, Callable, Optional, Union


def _write_log(message: str, filename: Optional[str] = None) -> None:
    """Записывает сообщение в файл или stdout.

    Args:
        message: Текст сообщения для записи.
        filename: Путь к файлу для записи. Если None, выводит в консоль.

    Returns:
        None: Функция ничего не возвращает.
    """
    if filename:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message)
    else:
        print(message, end="")


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования вызовов функций.

    Args:
        filename: Путь к лог-файлу. Если None, логи выводятся в консоль.

    Returns:
        Callable: Декорированная функция.

    Example:
        >>> @log(filename="app.log")
        ... def func(): ...
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обертка функции для логирования.

            Args:
                *args: Позиционные аргументы функции.
                **kwargs: Именованные аргументы функции.

            Returns:
                Any: Результат выполнения декорируемой функции.
            """
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            func_name = func.__name__
            try:
                result = func(*args, **kwargs)
                log_msg = f"{timestamp} - {func_name} ok\n"
                _write_log(log_msg, filename)
                return result
            except Exception as e:
                log_msg = f"{timestamp} - {func_name} error: {type(e).__name__}\nInputs: {args}, {kwargs}\n"
                _write_log(log_msg, filename)
                raise

        return wrapper

    return decorator
