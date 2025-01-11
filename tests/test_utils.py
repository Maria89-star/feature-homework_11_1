import os
from typing import Any

import pytest

from src.utils import get_operations_info


@pytest.fixture
def path_to_file():
    return os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "data", "operations.json"
    )


@pytest.fixture
def path_to_file_empty():
    return os.path.join(os.path.dirname(__file__), "data", "operations_empty.json")


def test_get_operations_info_empty(path_to_file_empty):
    assert get_operations_info(path_to_file_empty) == []


def get_info_json_object(capsys: Any) -> Any:
    get_operations_info(filename='../data/abdula.json')
    captured = capsys.readouterr()
    assert captured.out == 'FileNotFoundError'
