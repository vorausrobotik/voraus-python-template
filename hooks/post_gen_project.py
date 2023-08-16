import os
from pathlib import Path
from typing import Any, List

from git import Actor, Repo
from git.cmd import Git

os.system("isort .")
os.system("black .")

default_remote_url = (
    "{{ cookiecutter.url }}".replace("https://", "git@").replace(".com/", ".com:")
    + ".git"
)

print(
    "\n\n\033[1mOnly on project creation (not updates):\033[0m\n"
    "Initialize a Git repository by running the following commands:\n\n"
    "cd {{ cookiecutter.repo_name }} \\\n"
    "&& git init . \\\n"
    "&& git branch -M main \\\n"
    "&& git add --all \\\n"
    '&& git commit -m "Initial commit" \\\n'
    f"&& git remote add origin {default_remote_url} \\\n"
    "&& git push origin --all\n"
)
