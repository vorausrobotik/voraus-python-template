"""This module contains example tests."""

from pathlib import Path

from {{cookiecutter.import_name}}.example import my_function
from {{cookiecutter.import_name}} import get_app_name

def test_app_name() -> None:
    assert "{{ cookiecutter.package_name }}" == get_app_name()


def test_my_function() -> None:
    assert my_function() == 42


def test_use_test_resource(resource_dir: Path) -> None:
    assert resource_dir.joinpath("example_resource.txt").is_file()
