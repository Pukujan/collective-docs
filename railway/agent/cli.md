# CLI Reference
* Home
# CLI
## [Installing the CLI](#installing-the-cli)
Install the Railway CLI with agent support configured in one step (macOS, Linux, Windows via WSL):
This installs the CLI to `~/.railway/bin` and runs [`railway setup agent`](/cli/setup) to configure detected agent tools.
To install the CLI without agent configuration:
On Windows, use [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) with a Bash shell.
### [Other installation methods](#other-installation-methods)
#### [Homebrew (macOS)](#homebrew-macos)
#### [npm (macOS, Linux, Windows)](#npm-macos-linux-windows)
Requires Node.js version 16 or higher.
#### [Scoop (Windows)](#scoop-windows)
#### [Pre-built binaries](#pre-built-binaries)
Download [pre-built binaries](https://github.com/railwayapp/cli/releases/latest) from the [GitHub repository](https://github.com/railwayapp/cli).
#### [From source](#from-source)
Build from source using the instructions in the [GitHub repository](https://github.com/railwayapp/cli#from-source).
## [Authentication](#authentication)
Before using the CLI, authenticate with your Railway account:
For environments without a browser (e.g., SSH sessions), use browserless login:
### [Tokens](#tokens)
For CI/CD pipelines, set environment variables instead of interactive login:
* **Project Token**: Set `RAILWAY_TOKEN` for project-level actions
* **Account/Workspace Token**: Set `RAILWAY_API_TOKEN` for account-level actions
See [Tokens](/integrations/api#project-token) for more information.
## [Available commands](#available-commands)
### [Authentication](#authentication-1)
[login](/cli/login) · [logout](/cli/logout) · [whoami](/cli/whoami)
### [Project management](#project-management)
[init](/cli/init) · [link](/cli/link) · [unlink](/cli/unlink) · [list](/cli/list) · [status](/cli/status) · [open](/cli/open) · [project](/cli/project)
### [Deployment](#deployment)
[up](/cli/up) · [deploy](/cli/deploy) · [redeploy](/cli/redeploy) · [restart](/cli/restart) · [down](/cli/down) · [deployment](/cli/deployment) · [templates](/cli/templates) · [Deploying Guide](/cli/deploying)
### [Services](#services)
[add](/cli/add) · [service](/cli/service) · [scale](/cli/scale) · [delete](/cli/delete)
### [Variables](#variables)
[variable](/cli/variable)
### [Environments](#environments)
[environment](/cli/environment)
### [Local development](#local-development)
[run](/cli/run) · [shell](/cli/shell) · [dev](/cli/dev)
### [Logs & debugging](#logs--debugging)
[logs](/cli/logs) · [ssh](/cli/ssh) · [connect](/cli/connect) · [metrics](/cli/metrics)
### [Networking](#networking)
[domain](/cli/domain) · [cdn](/cli/cdn) · [waf](/cli/waf)
### [Volumes](#volumes)
[volume](/cli/volume)
### [Buckets](#buckets)
[bucket](/cli/bucket)
### [Functions](#functions)
[functions](/cli/functions)
### [Sandboxes](#sandboxes)
[sandbox](/cli/sandbox)
### [AI & agents](#ai--agents)
[agent](/cli/agent) · [setup](/cli/setup) · [mcp](/cli/mcp) · [skills](/cli/skills)
### [Utilities](#utilities)
[completion](/cli/completion) · [docs](/cli/docs) · [upgrade](/cli/upgrade) · [starship](/cli/starship)
## [Global options](#global-options)
These flags are available across multiple commands:
[TABLE]
 | Flag  Description  |
|  `-s, --service`  Target service (name or ID)  |
|  `-e, --environment`  Target environment (name or ID)  |
|  `--json`  Output in JSON format  |
|  `-y, --yes`  Skip confirmation prompts  |
|  `-h, --help`  Display help information  |
|  `-V, --version`  Display CLI version  |
[/TABLE]
See [Global Options](/cli/global-options) for more details.
## [SSH](#ssh)
The Railway CLI enables you to start a shell session inside your deployed Railway services:
Copy the exact command from the Railway dashboard by right-clicking on a service and selecting "Copy SSH Command".
See [railway ssh](/cli/ssh) for more details.
## [Contributing](#contributing)
The Railway CLI is open source. Contribute to the development of the Railway CLI by opening an issue or Pull Request on the [GitHub Repo](https://github.com/railwayapp/cli).
[Installing the CLI](#installing-the-cli)[Other installation methods](#other-installation-methods)[Homebrew (macOS)](#homebrew-macos)[npm (macOS, Linux, Windows)](#npm-macos-linux-windows)[Scoop (Windows)](#scoop-windows)[Pre-built binaries](#pre-built-binaries)[From source](#from-source)[Authentication](#authentication)[Tokens](#tokens)[Available commands](#available-commands)[Authentication](#authentication-1)[Project management](#project-management)[Deployment](#deployment)[Services](#services)[Variables](#variables)[Environments](#environments)[Local development](#local-development)[Logs & debugging](#logs--debugging)[Networking](#networking)[Volumes](#volumes)[Buckets](#buckets)[Functions](#functions)[Sandboxes](#sandboxes)[AI & agents](#ai--agents)[Utilities](#utilities)[Global options](#global-options)[SSH](#ssh)[Contributing](#contributing)### Ask AI about this page