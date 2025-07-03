from typing import Any

import pytest

from src.decorators import log


def test_log_to_console(capsys: Any) -> None:
    """
    Тест логирования в консоль.
    """

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result = add(1, 2)
    captured = capsys.readouterr()
    assert "add ok" in captured.out
    assert result == 3


def test_log_to_file(tmp_path: Any) -> None:
    """
    Тест логирования в файл.
    """
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def divide(a: int, b: int) -> float:
        return a / b

    result = divide(10, 2)
    assert result == 5
    assert "divide ok" in log_file.read_text()


def test_log_error_case(capsys: Any) -> None:
    """
    Тест логирования ошибок в декораторе.
    """

    @log()
    def fail_func() -> None:
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        fail_func()

    captured = capsys.readouterr()
    assert "fail_func error: ValueError" in captured.out
    assert "Inputs: (), {}" in captured.out


def test_log_to_file_error(tmp_path: Any) -> None:
    """
    Тест записи ошибок в файл.
    """
    log_file = tmp_path / "error.log"

    @log(filename=str(log_file))
    def error_func() -> None:
        raise TypeError("Test type error")

    with pytest.raises(TypeError):
        error_func()

    assert "error_func error: TypeError" in log_file.read_text()


def test_log_with_kwargs(capsys: Any) -> None:
    """
    Тест логирования функций с kwargs.
    """

    @log()
    def greet(name: str, greeting: str = "Hello") -> str:
        return f"{greeting}, {name}!"

    result = greet("Alice", greeting="Hi")
    captured = capsys.readouterr()
    assert "greet ok" in captured.out
    assert result == "Hi, Alice!"
