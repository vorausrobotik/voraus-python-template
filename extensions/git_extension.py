#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module contains a Jinja2 extension to retrieve git information."""

import subprocess

from jinja2 import nodes
from jinja2.ext import Extension
from jinja2.parser import Parser


class GitExtension(Extension):
    """The Jinja2 extension."""

    tags = {"gituser", "gitemail"}

    def parse(self, parser: Parser) -> nodes.Output:
        """Retrieves the git user name or email.

        Args:
            parser (Parser): The Jinja2 parser.

        Returns:
            nodes.Output: The git user name or email.
        """
        token = next(parser.stream)
        lineno = token.lineno

        git_user = self.call_method("_git_user", [], [], lineno=lineno)
        git_email = self.call_method("_git_email", [], [], lineno=lineno)

        if token.value == "gituser":
            return nodes.Output([git_user], lineno=lineno)

        return nodes.Output([git_email], lineno=lineno)

    def _git_user(self) -> str:
        """Returns the git user.

        Returns:
            str: The git user.
        """
        return (
            subprocess.check_output(["git", "config", "--get", "user.name"])
            .decode("utf-8")
            .strip()
        )

    def _git_email(self) -> str:
        """Returns the git email.

        Returns:
            str: The git email.
        """
        return (
            subprocess.check_output(["git", "config", "--get", "user.email"])
            .decode("utf-8")
            .strip()
        )
