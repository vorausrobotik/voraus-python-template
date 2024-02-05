"""Contains all application utility functions."""

from pytest import MonkeyPatch

from cookiecutter_pypackage import get_app_name, get_app_version


def test_get_app_name() -> None:
    assert "cookiecutter-pypackage" == get_app_name()


def test_get_app_version(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("cookiecutter_pypackage.__version__", "42.0.0")
    assert "42.0.0" == get_app_version()
