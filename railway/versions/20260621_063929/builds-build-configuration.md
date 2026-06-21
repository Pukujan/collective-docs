---
title: Build Configuration
source: railway
url: https://docs.railway.com/builds/build-configuration
fetched: 2026-06-21T06:39:24.370131
---

# Build Configuration

* [Home](/)
* svg]:size-3.5">
* [Build & deploy](/build-deploy)
* svg]:size-3.5">
* [Builds](/builds)
* svg]:size-3.5">
* Build configuration

# Build Configuration

On this pageRailway will build and deploy your code with zero configuration, but when necessary, there are several ways to configure this behavior to suit your needs.


## [Railpack](#railpack)


Railway uses [Railpack](https://railpack.com) to
build your code. It works with zero configuration, but can be customized using
[environment variables](/variables#service-variables) or a [config
file](https://railpack.com/config/file). Configuration options include:


* Language versions

* Build/install/start commands

* Mise and Apt packages to install

* Directories to cache


For a full list of configuration options, please view the [Railpack docs](https://railpack.com/config/environment-variables). You can find a complete list of languages we
support out of the box [here](/builds/railpack#supported-languages).


## [Customize the build command](#customize-the-build-command)


You can override the detected build command by setting a value in your service
settings. This is run after languages and packages have been installed.


![](https://res.cloudinary.com/railway/image/upload/v1743192207/docs/build-command_bwdprb.png)
## [Set the root directory](#set-the-root-directory)


The root directory defaults to `/` but can be changed for various use-cases like
[monorepo](/deployments/monorepo) projects.


![](https://res.cloudinary.com/railway/image/upload/v1743192841/docs/root-directory_nfzkfi.png)
When specified, all build and deploy
commands will operate within the defined root directory.


**Note:** The **Railway Config File** does not follow the **Root Directory** path. You have to specify the absolute path for the `railway.json` or `railway.toml` file, for example: `/backend/railway.toml`


## [Configure watch paths](#configure-watch-paths)


Watch paths are [gitignore-style](https://git-scm.com/docs/gitignore#_pattern_format) patterns
that can be used to trigger a new deployment based on what file paths have
changed.


![](https://res.cloudinary.com/railway/image/upload/v1743192841/docs/watch-paths_zv62py.png)
For example, a monorepo might want to only trigger builds if files are
changed in the `/packages/backend` directory.


When specified, any changes that
don't match the patterns will skip creating a new deployment. Multiple patterns
can be combined, one per line.


*Note, if a Root Directory is provided, patterns still operate from `/`. For a root directory of `/app`, `/app/**.js` would be used as a pattern to match files in the new root.*


Here are a few examples of common use-cases:


*Note, negations will only work if you include files in a preceding rule.*


## [Install specific packages using Railpack](#install-specific-packages-using-railpack)


[TABLE]
 | Environment variable  Description  |
|  `RAILPACK_PACKAGES`  A list of [Mise](https://mise.jdx.dev/) packages to install  |
|  `RAILPACK_BUILD_APT_PACKAGES`  Install additional Apt packages during build  |
|  `RAILPACK_DEPLOY_APT_PACKAGES`  Install additional Apt packages in the final image  |

[/TABLE]

See the [Railpack docs](https://railpack.com/config/environment-variables) for more information.


## [Procfiles](#procfiles)


Railpack automatically detects commands defined in
[Procfiles](https://railpack.com/config/procfile). Although this is not
recommended and specifing the start command directly in your service settings is
preferred.


## [Specify a custom install command](#specify-a-custom-install-command)


You can override the install command by setting the `RAILPACK_INSTALL_CMD`
environment variable in your service settings.


## [Disable build layer caching](#disable-build-layer-caching)


By default, Railway will cache build layers to provide faster build times. If
you have a need to disable this behavior, set the following environment variable
in your service:


## [Why isn't my build using cache?](#why-isnt-my-build-using-cache)


Since Railway's build system scales up and down in response to demand, cache hit
on builds is not guaranteed.


If you have a need for faster builds and rely on build cache to satisfy that
requirement, you should consider creating a pipeline to build your own image and
deploy your image directly.

[PreviousBuilds](/builds)[NextBuild and start commands](/builds/build-and-start-commands)### On this page

[Railpack](#railpack)[Customize the build command](#customize-the-build-command)[Set the root directory](#set-the-root-directory)[Configure watch paths](#configure-watch-paths)[Install specific packages using Railpack](#install-specific-packages-using-railpack)[Procfiles](#procfiles)[Specify a custom install command](#specify-a-custom-install-command)[Disable build layer caching](#disable-build-layer-caching)[Why isn't my build using cache?](#why-isnt-my-build-using-cache)### Ask AI about this page

Copy pageOpen in ChatGPTOpen in ClaudeOpen in Cursor[Edit this page on GitHub](https://github.com/railwayapp/docs/edit/main/content/docs/builds/build-configuration.md)Last updated Jun 20, 2026