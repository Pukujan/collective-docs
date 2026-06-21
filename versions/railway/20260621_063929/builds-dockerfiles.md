---
title: Dockerfiles on Railway
source: railway
url: https://docs.railway.com/builds/dockerfiles
fetched: 2026-06-21T06:39:25.089547
---

# Dockerfiles on Railway

* [Home](/)
* svg]:size-3.5">
* [Build & deploy](/build-deploy)
* svg]:size-3.5">
* [Builds](/builds)
* svg]:size-3.5">
* Dockerfiles

# Dockerfiles

On this pageUse a Dockerfile to instruct Railway how to build a service.


## [How it works](#how-it-works)


When building a service, Railway will look for and use a `Dockerfile` at the root of the source directory.


**Note:** For the automatic Dockerfile detection to work, the Dockerfile must be named `Dockerfile` with a capital D, otherwise Railway will not use it by default.


Railway notifies you when it's using the `Dockerfile` in the build process with the following message in the logs:


## [Custom Dockerfile path](#custom-dockerfile-path)


By default, we look for a file named `Dockerfile` in the root directory. If you want to use a custom filename or path, you can set a variable defining the path.


In your [service variables](/variables), set a variable named `RAILWAY_DOCKERFILE_PATH` to specify the path to the file.


For example, if your Dockerfile was called `Dockerfile.origin`, you would specify it like this:


If your Dockerfile is in another directory, specify it like this:


### [Use config as Code](#use-config-as-code)


You can also set your custom Dockerfile path using [config as code](/config-as-code).


## [Using variables at build time](#using-variables-at-build-time)


If you need to use the environment variables that Railway injects at build time, which include [variables that you define](/variables) and [Railway-provided variables](/variables#railway-provided-variables), you must specify them in the Dockerfile using the `ARG` command.


For example:


Be sure to declare your environment variables in the stage they are required in:


## [Cache mounts](#cache-mounts)


Railway supports cache mounts in your Dockerfile in the following format:


Replace `` with the id of the service.


p]:my-1 [&>p:first-child]:mt-0 [&>p:last-child]:mb-0 [&_a]:underline [&_a]:underline-offset-2 [&_a:hover]:opacity-80">Environment variables can't be used in cache mount IDs, since that is invalid syntax.


### [Target path](#target-path)


Unsure of what your target path should be? Check your language or runtime's documentation for the default cache directory path.


**Example**


For Python, the `PIP_CACHE_DIR` is `/root/.cache/pip`.


So the mount command is specified like this:


## [Docker compose](#docker-compose)


You can import services straight from your Docker Compose file! Just drag and drop your Compose file onto your [project canvas](/overview/the-basics#project--project-canvas), and your services (and any mounted volumes) will be auto-imported as staged changes. It's like magic, but with YAML instead of wands. 🪄


A quick heads-up: we don't support every possible Compose config just yet (because Rome wasn't built in a day). But don't worry, we're on it!

[PreviousSkipped builds](/builds/skipped-builds)[NextPrivate registries](/builds/private-registries)### On this page

[How it works](#how-it-works)[Custom Dockerfile path](#custom-dockerfile-path)[Use config as Code](#use-config-as-code)[Using variables at build time](#using-variables-at-build-time)[Cache mounts](#cache-mounts)[Target path](#target-path)[Docker compose](#docker-compose)### Ask AI about this page

Copy pageOpen in ChatGPTOpen in ClaudeOpen in Cursor[Edit this page on GitHub](https://github.com/railwayapp/docs/edit/main/content/docs/builds/dockerfiles.md)Last updated Jun 20, 2026