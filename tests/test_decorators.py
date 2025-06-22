# test_decorators.py
import os
import pytest
from src.decorators import log


def test_log_to_console(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(1, 2)
    captured = capsys.readouterr()
    assert "add ok" in captured.out
    assert result == 3


def test_log_to_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def divide(a, b):
        return a / b

    # Test successful execution
    result = divide(10, 2)
    assert result == 5
    assert "divide ok" in log_file.read_text()

    # Test error case
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    log_content = log_file.read_text()
    assert "divide error: ZeroDivisionError" in log_content
    assert "Inputs: (10, 0), {}" in log_content


def test_log_with_kwargs(capsys):
    @log()
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    result = greet("Alice", greeting="Hi")
    captured = capsys.readouterr()
    assert "greet ok" in captured.out
    assert result == "Hi, Alice!"