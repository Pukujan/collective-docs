---
title: CLI Reference
source: nixpacks
url: https://nixpacks.com/docs/cli
fetched: 2026-06-21T06:36:30.215521
---

# CLI Reference

# [CLI#](/docs/cli#cli)

The main Nixpacks commands are `build` and `plan`.

## [Build#](/docs/cli#build)

Create an image from an app source directory. The resulting image can then be run using Docker.

For example

```
nixpacks build ./path/to/app --name my-app

```

View all build options with

```
nixpacks build --help

```

### [Options#](/docs/cli#options)


[TABLE]
 |     |
|  `--install-cmd `, `-i`  Specify the install command  |
|  `--build-cmd `, `-b`  Specify the build command  |
|  `--start-cmd `, `-s`  Specify the start command  |
|  `--name `  Name for the built image  |
|  `--env `  Provide environment variables to your build.  |
|  `--pkgs `, `-p`  Provide additional Nix packages to install in the environment  |
|  `--apt `  Provide additional apt packages to install in the environment  |
|  `--libs `  Provide additional Nix libraries to install in the environment  |
|  `--tag `, `-t`  Additional tags to add to the output image  |
|  `--label `, `-l`  Additional labels to add to the output image  |
|  `--cache-key `  Unique identifier to use for the build cache  |
|  `--no-cache`  Disable caching for the build  |
|  `--docker-host`  Specify host for Docker client  |
|  `--docker-tls-verify`  Specify if Docker client should verify the TLS (Transport Layer Security) certificates of the Docker daemon when communicating over a secure connection  |
|  `--docker-cert-path`  Specify the path of your cert to docker if your connection is under TLS  |
|  `--cache-from`  Image to consider as cache sources  |
|  `--inline-cache`  Enable writing cache metadata into the output image  |
|  `--out `, `-o`  Save output directory instead of building it with Docker  |
|  `--platform `  Choosing the target platform for the target environment  |
|  `--config `  Location of the Nixpacks configuration file relative to the root of the app  |

[/TABLE]
#### [Environment Variables#](/docs/cli#environment-variables)

Environment variables can be provided in the format `FOO` or `FOO=bar`. If no equal sign is present then the value is pulled from the current environment.

#### [Labels#](/docs/cli#labels)

You can provide values to labels, just like Docker. For example, `--label org.opencontainers.image.source=https://github.com/owner/repo`.

## [Plan#](/docs/cli#plan)

The plan command will show the full set of options (nix packages, build cmd, start cmd, etc) that will be used to when building the app. This plan can be saved and used to build the app with the same configuration at a future date.

For example,

```
nixpacks plan examples/node

```

By default, the plan is output in JSON format. You can output in TOML format with the `--format toml` option. The generated plan will be outputted to stdout, while some providers expose recoverable errors to stderr.

View all plan options with

```
nixpacks plan --help

```

## [Help#](/docs/cli#help)

For a full list of CLI commands run

```
nixpacks --help

```