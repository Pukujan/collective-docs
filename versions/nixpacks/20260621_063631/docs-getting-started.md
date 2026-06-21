---
title: Getting Started
source: nixpacks
url: https://nixpacks.com/docs/getting-started
fetched: 2026-06-21T06:36:28.928407
---

# Getting Started

# [Getting Started#](/docs/getting-started#getting-started)

**⚠️ Maintenance Mode:** This project is currently in maintenance mode and is not under active development. We recommend using [Railpack](https://github.com/railwayapp/railpack) as a replacement.

To get started with Nixpacks you need an app that you want to build and package. You can bring your own or use one of the [many examples on GitHub](https://github.com/railwayapp/nixpacks/tree/main/examples).

## [1. Install#](/docs/getting-started#install)

```
brew install nixpacks

```

[View more installation options](/docs/install)

## [2. Build and package#](/docs/getting-started#build-and-package)

```
nixpacks build ./path/to/app --name my-app

```

This creates an image with the name `my-app`.

Nixpacks allows you to customize all options that are used to build the image. For example, you can add additional system packages and specify the build and start commands.

```
nixpacks build ./path/to/app --name my-app \
                             --pkgs cowsay \
                             --build-cmd ./build.sh \
                             --start-cmd "echo hello | cowsay"

```

## [3. Run the image#](/docs/getting-started#run-the-image)

```
docker run -it my-app

```

![Getting Started](/images/getting-started.png)