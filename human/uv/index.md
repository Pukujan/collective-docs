---
title: uv — Overview & Getting Started
source: uv
url: https://docs.astral.sh/uv/
fetched: 2026-06-21T06:40:55.261927
---

# uv — Overview & Getting Started

[

  ![logo](assets/logo-letter.svg)

    ](.)
    uv


      [


    uv

](https://github.com/astral-sh/uv)


    *

      *


    Introduction


      [


    Introduction


      ](.)


      Table of contents


  [


        Highlights


  ](#highlights)


        *
  [


        Installation


  ](#installation)


        *
  [


        Projects


  ](#projects)


        *
  [


        Scripts


  ](#scripts)


        *
  [


        Tools


  ](#tools)


        *
  [


        Python versions


  ](#python-versions)


        *
  [


        The pip interface


  ](#the-pip-interface)


        *
  [


        Learn more


  ](#learn-more)


    *


            [


    Getting started


            ](getting-started/)


    Getting started


      [


    Installation


      ](getting-started/installation/)


    *
      [


    First steps


      ](getting-started/first-steps/)


    *
      [


    Features


      ](getting-started/features/)


    *
      [


    Getting help


      ](getting-started/help/)


    *


            [


    Guides


            ](guides/)


    Guides


      [


    Installing Python


      ](guides/install-python/)


    *
      [


    Running scripts


      ](guides/scripts/)


    *
      [


    Using tools


      ](guides/tools/)


    *
      [


    Working on projects


      ](guides/projects/)


    *
      [


    Publishing packages


      ](guides/package/)


    *


            [


    Migration


            ](guides/migration/)


    Migration


      [


    From pip to a uv project


      ](guides/migration/pip-to-project/)


    *


            [


    Integrations


            ](guides/integration/)


    Integrations


      [


    Docker


      ](guides/integration/docker/)


    *
      [


    Jupyter


      ](guides/integration/jupyter/)


    *
      [


    marimo


      ](guides/integration/marimo/)


    *
      [


    GitHub Actions


      ](guides/integration/github/)


    *
      [


    GitLab CI/CD


      ](guides/integration/gitlab/)


    *
      [


    Pre-commit


      ](guides/integration/pre-commit/)


    *
      [


    PyTorch


      ](guides/integration/pytorch/)


    *
      [


    FastAPI


      ](guides/integration/fastapi/)


    *
      [


    Bazel


      ](guides/integration/bazel/)


    *
      [


    Azure Artifacts


      ](guides/integration/azure/)


    *
      [


    Google Artifact Registry


      ](guides/integration/google/)


    *
      [


    AWS CodeArtifact


      ](guides/integration/aws/)


    *
      [


    JFrog Artifactory


      ](guides/integration/jfrog/)


    *
      [


    Renovate


      ](guides/integration/renovate/)


    *
      [


    Dependabot


      ](guides/integration/dependabot/)


    *
      [


    AWS Lambda


      ](guides/integration/aws-lambda/)


    *
      [


    Coiled


      ](guides/integration/coiled/)


    *


            [


    Concepts


            ](concepts/)


    Concepts


            [


    Projects


            ](concepts/projects/)


    Projects


      [


    Structure and files


      ](concepts/projects/layout/)


    *
      [


    Creating projects


      ](concepts/projects/init/)


    *
      [


    Managing dependencies


      ](concepts/projects/dependencies/)


    *
      [


    Running commands


      ](concepts/projects/run/)


    *
      [


    Locking and syncing


      ](concepts/projects/sync/)


    *
      [


    Configuring projects


      ](concepts/projects/config/)


    *
      [


    Building distributions


      ](concepts/projects/build/)


    *
      [


    Exporting lockfiles


      ](concepts/projects/export/)


    *
      [


    Using workspaces


      ](concepts/projects/workspaces/)


    *
      [


    Tools


      ](concepts/tools/)


    *
      [


    Python versions


      ](concepts/python-versions/)


    *
      [


    Configuration files


      ](concepts/configuration-files/)


    *
      [


    Package indexes


      ](concepts/indexes/)


    *
      [


    Resolution


      ](concepts/resolution/)


    *
      [


    Build backend


      ](concepts/build-backend/)


    *


            [


    Authentication


            ](concepts/authentication/)


    Authentication


      [


    The auth CLI


      ](concepts/authentication/cli/)


    *
      [


    HTTP credentials


      ](concepts/authentication/http/)


    *
      [


    Git credentials


      ](concepts/authentication/git/)


    *
      [


    TLS certificates


      ](concepts/authentication/certificates/)


    *
      [


    Third-party services


      ](concepts/authentication/third-party/)


    *
      [


    Caching


      ](concepts/cache/)


    *
      [


    Preview features


      ](concepts/preview/)


    *


            [


    The pip interface


            ](pip/)


    The pip interface


      [


    Using environments


      ](pip/environments/)


    *
      [


    Managing packages


      ](pip/packages/)


    *
      [


    Inspecting environments


      ](pip/inspection/)


    *
      [


    Declaring dependencies


      ](pip/dependencies/)


    *
      [


    Locking environments


      ](pip/compile/)


    *
      [


    Compatibility with pip


      ](pip/compatibility/)


    *


            [


    Reference


            ](reference/)


    Reference


      [


    Commands


      ](reference/cli/)


    *
      [


    Settings


      ](reference/settings/)


    *
      [


    Environment variables


      ](reference/environment/)


    *
      [


    Storage


      ](reference/storage/)


    *
      [


    Installer options


      ](reference/installer/)


    *


            [


    Troubleshooting


            ](reference/troubleshooting/)


    Troubleshooting


      [


    Build failures


      ](reference/troubleshooting/build-failures/)


    *
      [


    Reproducible examples


      ](reference/troubleshooting/reproducible-examples/)


    *


            [


    Internals


            ](reference/internals/)


    Internals


      [


    Resolver


      ](reference/internals/resolver/)


    *
      [


    Workspace Metadata


      ](reference/internals/metadata/)


    *
      [


    Benchmarks


      ](reference/benchmarks/)


    *


            [


    Policies


            ](reference/policies/)


    Policies


      [


    Versioning


      ](reference/policies/versioning/)


    *
      [


    Platform support


      ](reference/policies/platforms/)


    *
      [


    Python support


      ](reference/policies/python/)


    *
      [


    Rust support


      ](reference/policies/rust/)


    *
      [


    License


      ](reference/policies/license/)


      Table of contents


        *
  [


        Highlights


  ](#highlights)


        *
  [


        Installation


  ](#installation)


        *
  [


        Projects


  ](#projects)


        *
  [


        Scripts


  ](#scripts)


        *
  [


        Tools


  ](#tools)


        *
  [


        Python versions


  ](#python-versions)


        *
  [


        The pip interface


  ](#the-pip-interface)


        *
  [


        Learn more


  ](#learn-more)


# [uv](#uv)


An extremely fast Python package and project manager, written in Rust.


  ![](https://github.com/astral-sh/uv/assets/1309177/629e59c0-9c6e-4013-9ad4-adb2bcf5080d#only-light)


  ![](https://github.com/astral-sh/uv/assets/1309177/03aa9163-1c79-4a87-a31d-7a9311ed9310#only-dark)


  Installing [Trio](https://trio.readthedocs.io/)'s dependencies with a warm cache.*


## [Highlights](#highlights)


* A single tool to replace `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, and
  more.

* [10-100x faster](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md) than `pip`.

* Provides [comprehensive project management](#projects), with a
  [universal lockfile](concepts/projects/layout/#the-lockfile).

* [Runs scripts](#scripts), with support for
  [inline dependency metadata](guides/scripts/#declaring-script-dependencies).

* [Installs and manages](#python-versions) Python versions.

* [Runs and installs](#tools) tools published as Python packages.

* Includes a [pip-compatible interface](#the-pip-interface) for a performance boost with a familiar
  CLI.

* Supports Cargo-style [workspaces](concepts/projects/workspaces/) for scalable projects.

* Disk-space efficient, with a [global cache](concepts/cache/) for dependency deduplication.

* Installable without Rust or Python via `curl` or `pip`.

* Supports macOS, Linux, and Windows.


uv is backed by [Astral](https://astral.sh), the creators of
[Ruff](https://github.com/astral-sh/ruff).


## [Installation](#installation)


Install uv with our official standalone installer:


macOS and LinuxWindows


```
`[](#__codelineno-0-1)$ curl -LsSf https://astral.sh/uv/install.sh | sh
`
```


```
`[](#__codelineno-1-1)PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
`
```


Then, check out the [first steps](getting-started/first-steps/) or read on for a brief overview.


Tip


uv may also be installed with pip, Homebrew, and more. See all of the methods on the
[installation page](getting-started/installation/).


## [Projects](#projects)


uv manages project dependencies and environments, with support for lockfiles, workspaces, and more,
similar to `rye` or `poetry`:


```
`[](#__codelineno-2-1)$ uv init example
[](#__codelineno-2-2)Initialized project `example` at `/home/user/example`
[](#__codelineno-2-3)
[](#__codelineno-2-4)$ cd example
[](#__codelineno-2-5)
[](#__codelineno-2-6)$ uv add ruff
[](#__codelineno-2-7)Creating virtual environment at: .venv
[](#__codelineno-2-8)Resolved 2 packages in 170ms
[](#__codelineno-2-9)   Built example @ file:///home/user/example
[](#__codelineno-2-10)Prepared 2 packages in 627ms
[](#__codelineno-2-11)Installed 2 packages in 1ms
[](#__codelineno-2-12) + example==0.1.0 (from file:///home/user/example)
[](#__codelineno-2-13) + ruff==0.5.4
[](#__codelineno-2-14)
[](#__codelineno-2-15)$ uv run ruff check
[](#__codelineno-2-16)All checks passed!
[](#__codelineno-2-17)
[](#__codelineno-2-18)$ uv lock
[](#__codelineno-2-19)Resolved 2 packages in 0.33ms
[](#__codelineno-2-20)
[](#__codelineno-2-21)$ uv sync
[](#__codelineno-2-22)Resolved 2 packages in 0.70ms
[](#__codelineno-2-23)Checked 1 package in 0.02ms
`
```


See the [project guide](guides/projects/) to get started.


uv also supports building and publishing projects, even if they're not managed with uv. See the
[packaging guide](guides/package/) to learn more.


## [Scripts](#scripts)


uv manages dependencies and environments for single-file scripts.


Create a new script and add inline metadata declaring its dependencies:


```
`[](#__codelineno-3-1)$ echo 'import requests; print(requests.get("https://astral.sh"))' > example.py
[](#__codelineno-3-2)
[](#__codelineno-3-3)$ uv add --script example.py requests
[](#__codelineno-3-4)Updated `example.py`
`
```


Then, run the script in an isolated virtual environment:


```
`[](#__codelineno-4-1)$ uv run example.py
[](#__codelineno-4-2)Reading inline script metadata from: example.py
[](#__codelineno-4-3)Installed 5 packages in 12ms
[](#__codelineno-4-4)
`
```


See the [scripts guide](guides/scripts/) to get started.


## [Tools](#tools)


uv executes and installs command-line tools provided by Python packages, similar to `pipx`.


Run a tool in an ephemeral environment using `uvx` (an alias for `uv tool run`):


```
`[](#__codelineno-5-1)$ uvx pycowsay 'hello world!'
[](#__codelineno-5-2)Resolved 1 package in 167ms
[](#__codelineno-5-3)Installed 1 package in 9ms
[](#__codelineno-5-4) + pycowsay==0.0.0.2
[](#__codelineno-5-5)  """
[](#__codelineno-5-6)
[](#__codelineno-5-7)  ------------
[](#__codelineno-5-8)
[](#__codelineno-5-9)  ------------
[](#__codelineno-5-10)   \   ^__^
[](#__codelineno-5-11)    \  (oo)\_______
[](#__codelineno-5-12)       (__)\       )\/\
[](#__codelineno-5-13)           ||----w |
[](#__codelineno-5-14)           ||     ||
`
```


Install a tool with `uv tool install`:


```
`[](#__codelineno-6-1)$ uv tool install ruff
[](#__codelineno-6-2)Resolved 1 package in 6ms
[](#__codelineno-6-3)Installed 1 package in 2ms
[](#__codelineno-6-4) + ruff==0.5.4
[](#__codelineno-6-5)Installed 1 executable: ruff
[](#__codelineno-6-6)
[](#__codelineno-6-7)$ ruff --version
[](#__codelineno-6-8)ruff 0.5.4
`
```


See the [tools guide](guides/tools/) to get started.


## [Python versions](#python-versions)


uv installs Python and allows quickly switching between versions.


Install multiple Python versions:


```
`[](#__codelineno-7-1)$ uv python install 3.10 3.11 3.12
[](#__codelineno-7-2)Searching for Python versions matching: Python 3.10
[](#__codelineno-7-3)Searching for Python versions matching: Python 3.11
[](#__codelineno-7-4)Searching for Python versions matching: Python 3.12
[](#__codelineno-7-5)Installed 3 versions in 3.42s
[](#__codelineno-7-6) + cpython-3.10.14-macos-aarch64-none
[](#__codelineno-7-7) + cpython-3.11.9-macos-aarch64-none
[](#__codelineno-7-8) + cpython-3.12.4-macos-aarch64-none
`
```


Download Python versions as needed:


```
`[](#__codelineno-8-1)$ uv venv --python 3.12.0
[](#__codelineno-8-2)Using CPython 3.12.0
[](#__codelineno-8-3)Creating virtual environment at: .venv
[](#__codelineno-8-4)Activate with: source .venv/bin/activate
[](#__codelineno-8-5)
[](#__codelineno-8-6)$ uv run --python [[email protected]](/cdn-cgi/l/email-protection) -- python
[](#__codelineno-8-7)Python 3.8.16 (a9dbdca6fc3286b0addd2240f11d97d8e8de187a, Dec 29 2022, 11:45:30)
[](#__codelineno-8-8)[PyPy 7.3.11 with GCC Apple LLVM 13.1.6 (clang-1316.0.21.2.5)] on darwin
[](#__codelineno-8-9)Type "help", "copyright", "credits" or "license" for more information.
[](#__codelineno-8-10)>>>>
`
```


Use a specific Python version in the current directory:


```
`[](#__codelineno-9-1)$ uv python pin 3.11
[](#__codelineno-9-2)Pinned `.python-version` to `3.11`
`
```


See the [installing Python guide](guides/install-python/) to get started.


## [The pip interface](#the-pip-interface)


uv provides a drop-in replacement for common `pip`, `pip-tools`, and `virtualenv` commands.


uv extends their interfaces with advanced features, such as dependency version overrides,
platform-independent resolutions, reproducible resolutions, alternative resolution strategies, and
more.


Migrate to uv without changing your existing workflows — and experience a 10-100x speedup — with the
`uv pip` interface.


Compile requirements into a platform-independent requirements file:


```
`[](#__codelineno-10-1)$ uv pip compile requirements.in \
[](#__codelineno-10-2)   --universal \
[](#__codelineno-10-3)   --output-file requirements.txt
[](#__codelineno-10-4)Resolved 43 packages in 12ms
`
```


Create a virtual environment:


```
`[](#__codelineno-11-1)$ uv venv
[](#__codelineno-11-2)Using CPython 3.12.3
[](#__codelineno-11-3)Creating virtual environment at: .venv
[](#__codelineno-11-4)Activate with: source .venv/bin/activate
`
```


Install the locked requirements:


```
`[](#__codelineno-12-1)$ uv pip sync requirements.txt
[](#__codelineno-12-2)Resolved 43 packages in 11ms
[](#__codelineno-12-3)Installed 43 packages in 208ms
[](#__codelineno-12-4) + babel==2.15.0
[](#__codelineno-12-5) + black==24.4.2
[](#__codelineno-12-6) + certifi==2024.7.4
[](#__codelineno-12-7) ...
`
```


See the [pip interface documentation](pip/) to get started.


## [Learn more](#learn-more)


See the [first steps](getting-started/first-steps/) or jump straight to the
[guides](guides/) to start using uv.


    March 13, 2026


  Back to top