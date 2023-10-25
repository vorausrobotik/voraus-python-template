#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""{{ cookiecutter.project_short_description }}"""

from importlib_metadata import PackageNotFoundError as _PackageNotFoundError
from importlib_metadata import version as _version

__module_name__ = "{{ cookiecutter.import_name }}"

try:  # pragma: no cover
    __version__ = _version(__module_name__)
except _PackageNotFoundError as error:  # pragma: no cover
    raise ModuleNotFoundError(
        f"Unable to determine version of package '{__module_name__}'. "
        "If you are on a local development system, use 'pip install -e .[dev]' in order to install the package. "
        "If you are on a productive system, this shouldn't happen. Please report a bug."
    ) from error
