# voraus Python Template

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

This is the template for the Python projects at [voraus robotik](https://vorausrobotik.com/).
By using [cruft](https://github.com/cruft/cruft/) and [cookiecutter](https://github.com/cookiecutter/cookiecutter),
existing projects are updated or new ones can be created.

> [!NOTE]
> This template heavily depends on the CI/CD infrastructure at voraus and won't work "out of the box".
It is more for orientation and customization to the individual needs of other open source projects.

> [!IMPORTANT]
> The default branch is [release/2.X](https://github.com/vorausrobotik/voraus-python-template/tree/release/2.X).
It contains a lot of breaking changes compared to the (old) [main](https://github.com/vorausrobotik/voraus-python-template/tree/main) branch.

## Table Of Contents
- [voraus Python Template](#voraus-python-template)
  - [Table Of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Creating a New Project](#creating-a-new-project)
  - [Updating an Existing Project](#updating-an-existing-project)
    - [v1.X Migration Guide](#v1x-migration-guide)
      - [Local Development Setup](#local-development-setup)
  - [About CI environments](#about-ci-environments)
    - [GitHub Actions](#github-actions)
    - [Jenkins prerequisites](#jenkins-prerequisites)
      - [Plugins, Variables \& Credentials](#plugins-variables--credentials)
      - [Build Image](#build-image)
  - [Improving This Template](#improving-this-template)
  - [License Notices](#license-notices)
  - [Need Help?](#need-help)


## Getting Started

The following tools are required to be installed on your system
- `uv` ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))
- `JFrog CLI` ([installation guide](https://jfrog.com/getcli/))

## Creating a New Project

Create a new project with

```
uvx cruft create https://github.com/vorausrobotik/voraus-python-template.git --checkout release/2.X
```

and follow the prompts.
Cruft uses [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.3/installation.html#install-cookiecutter) behind the scenes to generate the project.
The template will ask you for a name and email address to use for the maintainer of the project (the name and email address of your active Git profile is used by default).
Unless you know what you are doing, you should define a project name, e.g., "voraus example application", and go with the proposed default values.


## Updating an Existing Project

Cruft helps with updating projects that were originally created from a template.
Run `uvx cruft check` to check whether the project is out of sync with the template.
Run `uvx cruft update` to update the project.

The update is performed by looking at the template branch that is specified as `checkout` in the `cruft.json`.

### v1.X Migration Guide

#### Local Development Setup

Starting with v2.0, this template uses ([uv](https://docs.astral.sh/uv/)) instead of pip.

1) Delete your old python `venv` directory if it exists
2) Create a uv venv with `uv venv`
3) Install your package in editable mode with all development dependencies: `uv pip install -e . --group dev`
4) Make sure that you're updating your IDE interpreter to `.venv/bin/python`

## About CI environments
This template lets you choose between a [Jenkins](https://www.jenkins.io/) or [GitHub Actions](https://github.com/features/actions)
CI environment. Will they work out of the box for you? Probably not. But they'll give you a good starting point!

### GitHub Actions

The GitHub Actions workflows provided in this template offer a solid foundation for CI/CD pipelines.
However, additional configuration may be required depending on your deployment targets:

- **PyPI publishing**: Configure OIDC trust relationship or API tokens in repository secrets
- **JFrog Artifactory**: Set up OIDC authentication or configure access credentials
- **Private registries**: Add necessary authentication tokens and registry URLs to repository settings

Review the workflow files and customize them according to your specific requirements.

### Jenkins prerequisites

#### Plugins, Variables & Credentials
Your Jenkins CI environment needs the following plugins, variables and credentials:

- Plugins
  - [Kubernetes](https://plugins.jenkins.io/kubernetes/)
  - [Badges](https://plugins.jenkins.io/badge/)
  - [GitHub](https://plugins.jenkins.io/github/) (Optionally, only required for creating GitHub releases)
- Variables
  - `UV_INDEX`: If you use an internal proxy in order to resolve and deploy private python packages, you'll need to set the
    environment variable, either locally in the Jenkinsfile or globally in the Jenkins settings.
  - `JFROG_PLATFORM_URL`: If you use JFrog/Artifactory, this variable needs to be set.
- Credentials
  - All required credentials are defined and used in the [utility functions](./cookiecutter-pypackage/.jenkins/utils.groovy)
    - `jfrog-platform-credentials`: For the JFrog CLI
    - `github-app`: For creating GitHub releases


#### Build Image

The [Kubernetes Pod Spec](./cookiecutter-pypackage/.jenkins/pod-spec.yml) references the
```artifactory.vorausrobotik.com/docker/voraus-build-image``` docker build image which isn't publicly available (yet).
In order to get things running, you'll need to build and deploy an image on your own.
The [python:3.14-slim-trixie](https://hub.docker.com/_/python) docker image is a good starting point for this.
Moreover, you'll need to install the following packages:
- [uv](https://docs.astral.sh/uv/guides/integration/docker/)
- [JFrog CLI](https://jfrog.com/getcli/)
- [JReleaser](https://jreleaser.org/guide/latest/install.html)


## Improving This Template

You need to make the desired changes **in the template**.
Don't accidentally make your changes in the generated project because those changes will be overridden again.
Commit your changes so that they are used for the template generation in the next steps.
Non-committed changes won't be added to the template!
Run `uv run tox` to use the template to generate the sample package with your new changes.
Now, change into the generated package and validate that everything is working as expected:

```bash
cd cookiecutter-pypackage
uv run tox
uv run tox -e docs
uv run tox -e build
```
If everything is fine, (amend-)commit again and push all changes.

We want to run the Jenkinsfile that is in our sample project.
We can tell Jenkins where to find the Jenkinsfile but it will still use the repo folder as the working directory.
The test_config.yaml sets the `_debug` variable to "True" which modifies the Jenkinsfile such that every stage first
switches into the sample package directory.
This way, we can build our package on the Jenkins server and ensure that our changes didn't break the template.
Using the cookiecutter regularly does not prompt for `_debug` and it defaults to "False".

## License Notices

This project is licensed under the [MIT License](https://opensource.org/license/mit/). The commercial license,
which is applied by default in the template, only applies to `voraus robotik` internal projects.

## Need Help?

Having problems getting started? No worries, just open an issue!
