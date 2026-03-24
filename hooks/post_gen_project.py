import os
import shutil

default_remote_url = (
    "{{ cookiecutter.url }}".replace("https://", "git@").replace(".com/", ".com:")
    + ".git"
)

REMOVE_PATHS = []

match "{{cookiecutter.ci_tool}}":
    case "github_actions":
        REMOVE_PATHS.extend(
            [
                ".jenkins",
                "Jenkinsfile",
                ".groovylintrc.json",
            ]
        )
    case "jenkins":
        REMOVE_PATHS.extend(
            [
                *(
                    f".github/workflows/{workflow}.yml"
                    for workflow in [
                        "build",
                        "lint",
                        "pipeline",
                        "publish",
                        "setup",
                        "tests_and_coverage",
                    ]
                ),
            ]
        )
    case _:
        raise ValueError("Unknown CI tool")

if "{{cookiecutter.use_github_dependabot}}" != "True":
    REMOVE_PATHS.extend(
        [
            ".github/dependabot.yml",
        ]
    )

if "{{cookiecutter.use_github_pr_lint}}" != "True":
    REMOVE_PATHS.extend(
        [
            ".github/workflows/python_template_update_checks.yml",
            ".github/workflows/pr_lint.yml",
        ]
    )

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else shutil.rmtree(path)

print(
    "\n\n\033[1mOnly on project creation (not updates):\033[0m\n"
    "Initialize a Git repository by running the following commands:\n\n"
    "cd {{ cookiecutter.repo_name }} \\\n"
    "&& git init . \\\n"
    "&& git branch -M main \\\n"
    "&& uv sync \\\n"
    "&& git add --all \\\n"
    '&& git commit -m "chore: Initial commit" \\\n'
    f"&& git remote add origin {default_remote_url} \\\n"
    "&& git push origin --all\n"
)
