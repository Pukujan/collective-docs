# Vercel CLI — Overview & Commands
div]:m-0 [&>div]:max-w-none [&_button]:w-full">Search Docsspan]:text-xs [&>span]:!leading-[1.7em] py-0 h-5 px-1 min-w-5 min-h-5 ml-0.5 !m-0" data-geist-kbd="" data-version="v1">⌘ KStart
* [Getting started](/docs/getting-started-with-vercel)
* [Fundamentals](/docs/fundamentals)
* [Frameworks](/docs/frameworks)
* [Incremental Migration](/docs/incremental-migration)
* [Production Checklist](/docs/production-checklist)
Build AI apps
* [AI Gateway](/docs/ai-gateway)
* [AI SDK](/docs/ai-sdk)
* [MCP](/docs/mcp)
* [Vercel Connectbeta](/docs/connect)
* [evebeta](/docs/eve)
* [Agent Resources](/docs/agent-resources)
Run agents and backends
* [Functions](/docs/functions)
* [Fluid Compute](/docs/fluid-compute)
* [Routing Middleware](/docs/routing-middleware)
* [Cron Jobs](/docs/cron-jobs)
* [Queuesbeta](/docs/queues)
* [Workflows](/docs/workflows)
* [Sandbox](/docs/sandbox)
Ship and scale
* [Projects](/docs/projects)
* [Git](/docs/git)
* [Dropnew](/docs/drop)
* [CLI](/docs/cli)
* [Monorepos](/docs/monorepos)
* [Builds](/docs/builds)
* [Deployments](/docs/deployments)
* [Domains](/docs/domains)
* [Routing](/docs/routing)
* CDN
* [Microfrontends](/docs/microfrontends)
* Storage
* Integrations
* [Vercel Agent](/docs/agent)
Observe and improve
* Observability
* [Vercel Toolbar](/docs/vercel-toolbar)
* [Feature Flags](/docs/flags)
* [Rolling Releases](/docs/rolling-releases)
* [Instant Rollback](/docs/instant-rollback)
Secure and govern
* [Firewall](/docs/vercel-firewall)
* [Bot Management](/docs/bot-management)
* [BotID](/docs/botid)
* [Deployment Protection](/docs/deployment-protection)
* [Passportbeta](/docs/passport)
* [Identity & Access](/docs/rbac)
* [Networking](/docs/networking)
* [Security & Compliance](/docs/security)
Manage
* [Pricing](/docs/pricing)
* [Plans](/docs/plans)
* [Spend Management](/docs/spend-management)
* [Limits](/docs/limits)
* [Notifications](/docs/notifications)
* [Support Center](/docs/support-center)
Reference
* [Project Configuration](/docs/project-configuration)
* [REST API](/docs/rest-api)
* [Vercel SDK](/docs/rest-api/sdk)
* [Build Output API](/docs/build-output-api)
* [Webhooks](/docs/webhooks)
* [Marketplace APIs](/docs/integrations/create-integration/marketplace-api/reference)
* [Checks](/docs/checks)
* [Errors](/docs/errors)
* [Glossary](/docs/glossary)
CLI
* [Overview](/docs/cli)
* [Deploying from CLI](/docs/cli/deploying-from-cli)
* [Project Linking](/docs/cli/project-linking)
* [Telemetry](/docs/cli/about-telemetry)
* [Global Options](/docs/cli/global-options)
* [`vercel activity`](/docs/cli/activity)
* [`vercel agent`](/docs/cli/agent)
* [`vercel ai-gateway`](/docs/cli/ai-gateway)
* [`vercel alerts`](/docs/cli/alerts)
* [`vercel alias`](/docs/cli/alias)
* [`vercel api`beta](/docs/cli/api)
* [`vercel bisect`](/docs/cli/bisect)
* [`vercel blob`](/docs/cli/blob)
* [`vercel build`](/docs/cli/build)
* [`vercel buy`](/docs/cli/buy)
* [`vercel cache`](/docs/cli/cache)
* [`vercel certs`](/docs/cli/certs)
* [`vercel connect`beta](/docs/cli/connect)
* [`vercel contract`](/docs/cli/contract)
* [`vercel crons`beta](/docs/cli/crons)
* [`vercel curl`beta](/docs/cli/curl)
* [`vercel deploy`](/docs/cli/deploy)
* [`vercel deploy-hooks`](/docs/cli/deploy-hooks)
* [`vercel dev`](/docs/cli/dev)
* [`vercel dns`](/docs/cli/dns)
* [`vercel domains`](/docs/cli/domains)
* [`vercel edge-config`](/docs/cli/edge-config)
* [`vercel env`](/docs/cli/env)
* [`vercel firewall`](/docs/cli/firewall)
* [`vercel flags`](/docs/cli/flags)
* [`vercel git`](/docs/cli/git)
* [`vercel guidance`](/docs/cli/guidance)
* [`vercel help`](/docs/cli/help)
* [`vercel httpstat`beta](/docs/cli/httpstat)
* [`vercel init`](/docs/cli/init)
* [`vercel inspect`](/docs/cli/inspect)
* [`vercel install`](/docs/cli/install)
* [`vercel integration`](/docs/cli/integration)
* [`vercel link`](/docs/cli/link)
* [`vercel list`](/docs/cli/list)
* [`vercel login`](/docs/cli/login)
* [`vercel logout`](/docs/cli/logout)
* [`vercel logs`](/docs/cli/logs)
* [`vercel mcp`](/docs/cli/mcp)
* [`vercel metrics`](/docs/cli/metrics)
* [`vercel microfrontends`](/docs/cli/microfrontends)
* [`vercel oauth-apps`](/docs/cli/oauth-apps)
* [`vercel open`](/docs/cli/open)
* [`vercel project`](/docs/cli/project)
* [`vercel promote`](/docs/cli/promote)
* [`vercel pull`](/docs/cli/pull)
* [`vercel redeploy`](/docs/cli/redeploy)
* [`vercel redirects`](/docs/cli/redirects)
* [`vercel remove`](/docs/cli/remove)
* [`vercel rollback`](/docs/cli/rollback)
* [`vercel rolling-release`](/docs/cli/rolling-release)
* [`vercel routes`](/docs/cli/routes)
* [`vercel sandbox`](/docs/cli/sandbox)
* [`vercel skills`](/docs/cli/skills)
* [`vercel switch`](/docs/cli/switch)
* [`vercel target`](/docs/cli/target)
* [`vercel teams`](/docs/cli/teams)
* [`vercel telemetry`](/docs/cli/telemetry)
* [`vercel tokens`](/docs/cli/tokens)
* [`vercel traces`](/docs/cli/traces)
* [`vercel upgrade`](/docs/cli/upgrade)
* [`vercel usage`](/docs/cli/usage)
* [`vercel webhooks`beta](/docs/cli/webhooks)
* [`vercel whoami`](/docs/cli/whoami)
Copy pageCopy page# p]:m-0">Vercel CLI Overview
Copy pageCopy pageVercel gives you multiple ways to interact with and configure your Vercel Projects. With the command-line interface (CLI) you can interact with the Vercel platform using a terminal, or through an automated system, enabling you to [retrieve logs](/docs/cli/logs), manage [certificates](/docs/cli/certs), replicate your deployment environment [locally](/docs/cli/dev), manage Domain Name System (DNS) [records](/docs/cli/dns), and more.
If you'd like to interface with the platform programmatically, check out the [REST API documentation](/docs/rest-api).
## p]:m-0" href="#installing-vercel-cli">Installing Vercel CLI[](#installing-vercel-cli)
To download and install Vercel CLI, run the following command:
Terminal```
`pnpm i -g vercel`
```
## p]:m-0" href="#updating-vercel-cli">Updating Vercel CLI[](#updating-vercel-cli)
When there is a new release of Vercel CLI, running any command will show you a message letting you know that an update is available.
If you have installed our command-line interface through [npm](http://npmjs.org/) or [Yarn](https://yarnpkg.com), the easiest way to update it is by running the installation command yet again.
Terminal```
`pnpm i -g vercel@latest`
```
If you see permission errors, please read npm's [official guide](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally). Yarn depends on the same configuration as npm.
## p]:m-0" href="#checking-the-version">Checking the version[](#checking-the-version)
The `--version` option can be used to verify the version of Vercel CLI currently being used.
terminal```
`vercel --version`
```
Using the `vercel` command with the `--version` option.
## p]:m-0" href="#using-in-a-ci/cd-environment">Using in a CI/CD environment[](#using-in-a-ci/cd-environment)
Vercel CLI requires you to log in and authenticate before accessing resources or performing administrative tasks. In a terminal environment, you can use [`vercel login`](/docs/cli/login), which requires manual input. In a CI/CD environment where manual input is not possible, you can create a token on your [tokens page](/account/tokens) and then authenticate using one of these methods:
li::marker]:text-gray-500">
* svg]:inline-flex last:mb-0">Set the `VERCEL_TOKEN` environment variable
* svg]:inline-flex last:mb-0">Pass the [`--token` option](/docs/cli/global-options#token) to the command
Using the `VERCEL_TOKEN` environment variable is recommended for CI/CD because it avoids exposing the token in command-line arguments, which can be visible in process lists and logs. If both are provided, the `--token` flag takes precedence over the environment variable.
## p]:m-0" href="#experimental-native-cli-binaries">Experimental native CLI binaries[](#experimental-native-cli-binaries)
Native CLI binaries are also available as an experimental opt-in install.
Native CLI binaries can reduce setup in environments where installing and maintaining Node.js is unnecessary or inconvenient, including lightweight containers, CI jobs, or managed developer workspaces.
To install the native binary, run:
terminal```
`pnpm i -g @vercel/vc-native -f`
```
The `-f` flag is required because the native package installs the same global bin names as the standard CLI. It allows pnpm to replace existing global `vercel` and `vc` bin links. Once installed, `vercel` and `vc` run the native binary matched to your OS and CPU architecture, across macOS, Linux, and Windows on x64 and arm64.
Platform-specific packages are also available when you need a specific binary:
terminal```
`pnpm i -g @vercel/vc-native-darwin-x64 -f`
```
## p]:m-0" href="#available-commands">Available Commands[](#available-commands)
### p]:m-0" href="#activity">activity[](#activity)
View activity events for your Vercel project or team, filtered by type, date range, and project.
```
`vercel activity
vercel activity ls --all --since 30d
vercel activity ls --type deployment --since 7d`
```
[Learn more about the activity command](/docs/cli/activity)
### p]:m-0" href="#agent">agent[](#agent)
Generate an `AGENTS.md` file in the current project with Vercel deployment best practices for coding agents.
```
`vercel agent init
vercel agent init --yes`
```
[Learn more about the agent command](/docs/cli/agent)
### p]:m-0" href="#ai-gateway">ai-gateway[](#ai-gateway)
Manage [AI Gateway](/docs/ai-gateway) resources, including API keys, from the CLI.
```
`vercel ai-gateway api-keys create
vercel ai-gateway api-keys create --name my-key --budget 500 --refresh-period monthly`
```
[Learn more about the ai-gateway command](/docs/cli/ai-gateway)
### p]:m-0" href="#alerts">alerts[](#alerts)
List recent alerts for a linked project, a specific project, or an entire team.
```
`vercel alerts
vercel alerts --all
vercel alerts --project [project-name]`
```
[Learn more about the alerts command](/docs/cli/alerts)
### p]:m-0" href="#alias">alias[](#alias)
Apply custom domain aliases to your Vercel deployments.
```
`vercel alias set [deployment-url] [custom-domain]
vercel alias rm [custom-domain]
vercel alias ls`
```
[Learn more about the alias command](/docs/cli/alias)
### p]:m-0" href="#api">api[](#api)
Make authenticated HTTP requests to the Vercel API from your terminal. This is a beta command.
```
`vercel api [endpoint]
vercel api /v2/user
vercel api /v9/projects -X POST -F name=my-project`
```
[Learn more about the api command](/docs/cli/api)
### p]:m-0" href="#bisect">bisect[](#bisect)
Perform a binary search on your deployments to help surface issues.
```
`vercel bisect
vercel bisect --good [deployment-url] --bad [deployment-url]`
```
[Learn more about the bisect command](/docs/cli/bisect)
### p]:m-0" href="#blob">blob[](#blob)
Interact with Vercel Blob storage to upload, download, list, delete, and copy files.
```
`vercel blob list
vercel blob put [path-to-file]
vercel blob get [url-or-pathname]
vercel blob del [url-or-pathname]
vercel blob copy [from-url] [to-pathname]`
```
[Learn more about the blob command](/docs/cli/blob)
### p]:m-0" href="#build">build[](#build)
Build a Vercel Project locally or in your own CI environment.
```
`vercel build
vercel build --prod`
```
[Learn more about the build command](/docs/cli/build)
### p]:m-0" href="#buy">buy[](#buy)
Purchase Vercel products like credits, addons, subscriptions, and domains directly from the CLI.
```
`vercel buy credits v0 100
vercel buy addon siem 1
vercel buy pro
vercel buy domain example.com`
```
[Learn more about the buy command](/docs/cli/buy)
### p]:m-0" href="#cache">cache[](#cache)
Manage cache for your project (CDN cache and Data cache).
```
`vercel cache purge
vercel cache purge --type cdn
vercel cache purge --type data
vercel cache invalidate --tag foo
vercel cache dangerously-delete --tag foo`
```
[Learn more about the cache command](/docs/cli/cache)
### p]:m-0" href="#certs">certs[](#certs)
Manage certificates for your domains.
```
`vercel certs ls
vercel certs issue [domain]
vercel certs rm [certificate-id]`
```
[Learn more about the certs command](/docs/cli/certs)
### p]:m-0" href="#connect">connect[](#connect)
Manage connectors: create, list, attach to projects, request runtime tokens, and remove them. This is a beta command.
```
`vercel connect create type>
vercel connect list
vercel connect token id>
vercel connect attach id>
vercel connect detach id>
vercel connect update id>
vercel connect remove id>
vercel connect open id>`
```
[Learn more about the connect command](/docs/cli/connect)
### p]:m-0" href="#contract">contract[](#contract)
View contract commitment information for your Vercel account.
```
`vercel contract
vercel contract --format json`
```
[Learn more about the contract command](/docs/cli/contract)
### p]:m-0" href="#crons">crons[](#crons)
Manage [Cron Jobs](/docs/cron-jobs) for a project: add cron entries to `vercel.json`, list them, and trigger them on demand. This command is in beta.
```
`vercel crons ls
vercel crons add --path /api/cron --schedule "0 10 * * *"
vercel crons run /api/cron`
```
[Learn more about the crons command](/docs/cli/crons)
### p]:m-0" href="#curl">curl[](#curl)
Make HTTP requests to your Vercel deployments with automatic deployment protection bypass. This is a beta command.
```
`vercel curl [path]
vercel curl /api/hello
vercel curl /api/data --deployment [deployment-url]`
```
[Learn more about the curl command](/docs/cli/curl)
### p]:m-0" href="#deploy">deploy[](#deploy)
Deploy your Vercel projects. Default command when no subcommand is specified.
```
`vercel
vercel deploy
vercel deploy --prod`
```
[Learn more about the deploy command](/docs/cli/deploy)
### p]:m-0" href="#deploy-hooks">deploy-hooks[](#deploy-hooks)
Manage [Deploy Hooks](/docs/deploy-hooks): list, create, and remove deploy hook URLs that trigger new deployments when called.
```
`vercel deploy-hooks ls
vercel deploy-hooks create cms-rebuild --ref main
vercel deploy-hooks rm hook_abc123`
```
[Learn more about the deploy-hooks command](/docs/cli/deploy-hooks)
### p]:m-0" href="#dev">dev[](#dev)
Replicate the Vercel deployment environment locally and test your project.
```
`vercel dev
vercel dev --port 3000`
```
[Learn more about the dev command](/docs/cli/dev)
### p]:m-0" href="#dns">dns[](#dns)
Manage your DNS records for your domains.
```
`vercel dns ls [domain]
vercel dns add [domain] [name] [type] [value]
vercel dns rm [record-id]`
```
[Learn more about the dns command](/docs/cli/dns)
### p]:m-0" href="#domains">domains[](#domains)
Buy, sell, transfer, and manage your domains.
```
`vercel domains ls
vercel domains add [domain] [project]
vercel domains rm [domain]
vercel domains buy [domain]
vercel domains price [domain] [...domain]
vercel domains check [domain] [...domain]`
```
[Learn more about the domains command](/docs/cli/domains)
### p]:m-0" href="#edge-config">edge-config[](#edge-config)
Manage [Edge Config](/docs/edge-config) stores: list, create, inspect, update, remove, and manage items and read tokens.
```
`vercel edge-config list
vercel edge-config add flags
vercel edge-config items flags --key betaUiEnabled
vercel edge-config tokens flags --add "Production read"`
```
[Learn more about the edge-config command](/docs/cli/edge-config)
### p]:m-0" href="#env">env[](#env)
Manage environment variables in your Vercel Projects.
```
`vercel env ls
vercel env add [name] [environment]
vercel env update [name] [environment]
vercel env rm [name] [environment]
vercel env pull [file]
vercel env run -- command>`
```
[Learn more about the env command](/docs/cli/env)
### p]:m-0" href="#firewall">firewall[](#firewall)
Manage your Vercel Firewall: view changes, publish, manage IP blocks, system bypass entries, custom rules, attack mode, and system mitigations.
```
`vercel firewall overview
vercel firewall publish
vercel firewall ip-blocks block ip>
vercel firewall rules list
vercel firewall attack-mode enable`
```
[Learn more about the firewall command](/docs/cli/firewall)
### p]:m-0" href="#flags">flags[](#flags)
Manage feature flags for your Vercel Project.
```
`vercel flags list
vercel flags create [slug]
vercel flags set [flag] --environment [environment] --variant [variant]
vercel flags open [flag]`
```
[Learn more about the flags command](/docs/cli/flags)
### p]:m-0" href="#git">git[](#git)
Manage your Git provider connections.
```
`vercel git ls
vercel git connect
vercel git disconnect [provider]`
```
[Learn more about the git command](/docs/cli/git)
### p]:m-0" href="#guidance">guidance[](#guidance)
Enable or disable guidance messages shown after CLI commands.
```
`vercel guidance enable
vercel guidance disable
vercel guidance status`
```
[Learn more about the guidance command](/docs/cli/guidance)
### p]:m-0" href="#help">help[](#help)
Get information about all available Vercel CLI commands.
```
`vercel help
vercel help [command]`
```
[Learn more about the help command](/docs/cli/help)
### p]:m-0" href="#httpstat">httpstat[](#httpstat)
Visualize HTTP request timing statistics for your Vercel deployments with automatic deployment protection bypass.
```
`vercel httpstat [path]
vercel httpstat /api/hello
vercel httpstat /api/data --deployment [deployment-url]`
```
[Learn more about the httpstat command](/docs/cli/httpstat)
### p]:m-0" href="#init">init[](#init)
Initialize example Vercel Projects locally from the examples repository.
```
`vercel init
vercel init [project-name]`
```
[Learn more about the init command](/docs/cli/init)
### p]:m-0" href="#inspect">inspect[](#inspect)
Retrieve information about your Vercel deployments.
```
`vercel inspect [deployment-id-or-url]
vercel inspect [deployment-id-or-url] --logs
vercel inspect [deployment-id-or-url] --wait`
```
[Learn more about the inspect command](/docs/cli/inspect)
### p]:m-0" href="#install">install[](#install)
Install a marketplace integration and provision a resource. Alias for `vercel integration add`.
```
`vercel install integration-name>`
```
[Learn more about the install command](/docs/cli/install)
### p]:m-0" href="#integration">integration[](#integration)
Manage marketplace integrations: provision resources, discover available integrations, view setup guides, check balances, and manage individual resources with the nested `resource` subcommand.
```
`vercel integration add integration-name> [--claim | --no-claim]
vercel integration list [project]
vercel integration discover
vercel integration guide integration-name>
vercel integration balance integration-name>
vercel integration open integration-name> [resource-name]
vercel integration remove integration-name>
vercel integration resource connect resource-name> [project]
vercel integration resource disconnect resource-name> [project]
vercel integration resource remove resource-name>
vercel integration resource create-threshold resource-name> minimum> spend> limit>
vercel integration resource claim [resource-name]`
```
The `resource` subcommand is also available as `vercel integration-resource ` and `vc ir ` (backward-compatible aliases).
[Learn more about the integration command](/docs/cli/integration)
### p]:m-0" href="#link">link[](#link)
Link a local directory to a Vercel Project.
```
`vercel link
vercel link [path-to-directory]`
```
[Learn more about the link command](/docs/cli/link)
### p]:m-0" href="#list">list[](#list)
List recent deployments for the current Vercel Project.
```
`vercel list
vercel list [project-name]`
```
[Learn more about the list command](/docs/cli/list)
### p]:m-0" href="#login">login[](#login)
Login to your Vercel account through CLI.
```
`vercel login
vercel login [email]
vercel login --github`
```
[Learn more about the login command](/docs/cli/login)
### p]:m-0" href="#logout">logout[](#logout)
Logout from your Vercel account through CLI.
```
`vercel logout`
```
[Learn more about the logout command](/docs/cli/logout)
### p]:m-0" href="#logs">logs[](#logs)
List runtime logs for a specific deployment.
```
`vercel logs [deployment-url]
vercel logs [deployment-url] --follow`
```
[Learn more about the logs command](/docs/cli/logs)
### p]:m-0" href="#mcp">mcp[](#mcp)
Set up MCP client configuration for your Vercel Project.
```
`vercel mcp
vercel mcp --project`
```
[Learn more about the mcp command](/docs/cli/mcp)
### p]:m-0" href="#metrics">metrics[](#metrics)
Query observability metrics and inspect available metrics, dimensions, and aggregations.
```
`vercel metrics vercel.request.count
vercel metrics schema
vercel metrics schema vercel.request`
```
[Learn more about the metrics command](/docs/cli/metrics)
### p]:m-0" href="#microfrontends">microfrontends[](#microfrontends)
Work with microfrontends configuration.
```
`vercel microfrontends pull
vercel microfrontends pull --dpl [deployment-id]`
```
[Learn more about the microfrontends command](/docs/cli/microfrontends)
### p]:m-0" href="#oauth-apps">oauth-apps[](#oauth-apps)
Register Vercel Apps (OAuth) and manage team installations: register new apps, list and dismiss installation requests, install apps with permissions, and uninstall them.
```
`vercel oauth-apps list-requests
vercel oauth-apps register --name "My App" --slug my-app --redirect-uri https://app.example.com/oauth/callback
vercel oauth-apps install --client-id cl_abc --permission read:project
vercel oauth-apps remove inst_abc123 --yes`
```
[Learn more about the oauth-apps command](/docs/cli/oauth-apps)
### p]:m-0" href="#open">open[](#open)
Open your current project in the Vercel Dashboard.
```
`vercel open`
```
[Learn more about the open command](/docs/cli/open)
### p]:m-0" href="#project">project[](#project)
List, add, inspect, remove, and manage your Vercel Projects.
```
`vercel project ls
vercel project add
vercel project rm
vercel project inspect [project-name]`
```
[Learn more about the project command](/docs/cli/project)
### p]:m-0" href="#promote">promote[](#promote)
Promote an existing deployment to be the current deployment.
```
`vercel promote [deployment-id-or-url]
vercel promote status [project]`
```
[Learn more about the promote command](/docs/cli/promote)
### p]:m-0" href="#pull">pull[](#pull)
Update your local project with remote environment variables and project settings.
```
`vercel pull
vercel pull --environment=production`
```
[Learn more about the pull command](/docs/cli/pull)
### p]:m-0" href="#redeploy">redeploy[](#redeploy)
Rebuild and redeploy an existing deployment.
```
`vercel redeploy [deployment-id-or-url]`
```
[Learn more about the redeploy command](/docs/cli/redeploy)
### p]:m-0" href="#redirects">redirects[](#redirects)
Manage project-level redirects.
```
`vercel redirects list
vercel redirects add /old /new --status 301
vercel redirects upload redirects.csv --overwrite
vercel redirects promote version-id>`
```
[Learn more about the redirects command](/docs/cli/redirects)
### p]:m-0" href="#remove">remove[](#remove)
Remove deployments either by ID or for a specific Vercel Project.
```
`vercel remove [deployment-url]
vercel remove [project-name]`
```
[Learn more about the remove command](/docs/cli/remove)
### p]:m-0" href="#rollback">rollback[](#rollback)
Roll back production deployments to previous deployments.
```
`vercel rollback
vercel rollback [deployment-id-or-url]
vercel rollback status [project]`
```
[Learn more about the rollback command](/docs/cli/rollback)
### p]:m-0" href="#rolling-release">rolling-release[](#rolling-release)
Manage your project's rolling releases to gradually roll out new deployments.
```
`vercel rolling-release configure --cfg='[config]'
vercel rolling-release start --dpl=[deployment-id]
vercel rolling-release approve --dpl=[deployment-id]
vercel rolling-release complete --dpl=[deployment-id]`
```
[Learn more about the rolling-release command](/docs/cli/rolling-release)
### p]:m-0" href="#routes">routes[](#routes)
Manage project-level routing rules for your Vercel Project.
```
`vercel routes list
vercel routes add --ai "Rewrite /api/* to https://backend.internal/*"
vercel routes edit "API Proxy" --dest "https://new-api.example.com/:path*"
vercel routes publish`
```
[Learn more about the routes command](/docs/cli/routes)
### p]:m-0" href="#sandbox">sandbox[](#sandbox)
Interact with [Vercel Sandbox](/docs/sandbox): list, create, connect, and manage sandboxes from the terminal. See the [Sandbox CLI Reference](/docs/sandbox/cli-reference) for the full surface.
```
`vercel sandbox list
vercel sandbox create --connect`
```
[Learn more about the sandbox command](/docs/cli/sandbox)
### p]:m-0" href="#skills">skills[](#skills)
Discover agent skills relevant to your project, or search the skill catalog.
```
`vercel skills
vercel skills nextjs
vercel skills nextjs --json`
```
[Learn more about the skills command](/docs/cli/skills)
### p]:m-0" href="#switch">switch[](#switch)
Switch between different team scopes.
```
`vercel switch
vercel switch [team-name]`
```
[Learn more about the switch command](/docs/cli/switch)
### p]:m-0" href="#target">target[](#target)
Manage custom environments (targets) and use the `--target` flag on relevant commands.
```
`vercel target list
vercel target ls
vercel deploy --target=staging`
```
[Learn more about the target command](/docs/cli/target)
### p]:m-0" href="#teams">teams[](#teams)
List, add, remove, and manage your teams.
```
`vercel teams list
vercel teams add
vercel teams invite [email]`
```
[Learn more about the teams command](/docs/cli/teams)
### p]:m-0" href="#telemetry">telemetry[](#telemetry)
Enable or disable telemetry collection.
```
`vercel telemetry status
vercel telemetry enable
vercel telemetry disable`
```
[Learn more about the telemetry command](/docs/cli/telemetry)
### p]:m-0" href="#tokens">tokens[](#tokens)
Manage your personal Vercel authentication tokens: list, create, and revoke API tokens.
```
`vercel tokens ls
vercel tokens add "CI deploy"
vercel tokens rm tok_abc123`
```
[Learn more about the tokens command](/docs/cli/tokens)
### p]:m-0" href="#traces">traces[](#traces)
Inspect request traces for your project.
```
`vercel traces get [request-id]
vercel traces [request-id]
vercel traces get [request-id] --open --view=tree`
```
[Learn more about the traces command](/docs/cli/traces)
### p]:m-0" href="#upgrade">upgrade[](#upgrade)
Upgrade the Vercel CLI to the latest version and manage automatic updates.
```
`vercel upgrade
vercel upgrade --dry-run
vercel upgrade --enable-auto
vercel upgrade --format=json`
```
[Learn more about the upgrade command](/docs/cli/upgrade)
### p]:m-0" href="#usage">usage[](#usage)
View billing usage and costs for your Vercel account.
```
`vercel usage
vercel usage --from 2025-01-01 --to 2025-01-31
vercel usage --breakdown daily`
```
[Learn more about the usage command](/docs/cli/usage)
### p]:m-0" href="#webhooks">webhooks[](#webhooks)
Manage webhooks for your account. This command is in beta.
```
`vercel webhooks list
vercel webhooks get id>
vercel webhooks create url> --event event>
vercel webhooks rm id>`
```
[Learn more about the webhooks command](/docs/cli/webhooks)
### p]:m-0" href="#whoami">whoami[](#whoami)
Display the username of the currently logged in user.
```
`vercel whoami`
```
[Learn more about the whoami command](/docs/cli/whoami)
* [Installing Vercel CLI](#installing-vercel-cli)
* [Updating Vercel CLI](#updating-vercel-cli)
* [Checking the version](#checking-the-version)
* [Using in a CI/CD environment](#using-in-a-ci/cd-environment)
* [Experimental native CLI binaries](#experimental-native-cli-binaries)
* [Available Commands](#available-commands)
* [activity](#activity)
* [agent](#agent)
* [ai-gateway](#ai-gateway)
* [alerts](#alerts)
* [alias](#alias)
* [api](#api)
* [bisect](#bisect)
* [blob](#blob)
* [build](#build)
* [buy](#buy)
* [cache](#cache)
* [certs](#certs)
* [connect](#connect)
* [contract](#contract)
* [crons](#crons)
* [curl](#curl)
* [deploy](#deploy)
* [deploy-hooks](#deploy-hooks)
* [dev](#dev)
* [dns](#dns)
* [domains](#domains)
* [edge-config](#edge-config)
* [env](#env)
* [firewall](#firewall)
* [flags](#flags)
* [git](#git)
* [guidance](#guidance)
* [help](#help)
* [httpstat](#httpstat)
* [init](#init)
* [inspect](#inspect)
* [install](#install)
* [integration](#integration)
* [link](#link)
* [list](#list)
* [login](#login)
* [logout](#logout)
* [logs](#logs)
* [mcp](#mcp)
* [metrics](#metrics)
* [microfrontends](#microfrontends)
* [oauth-apps](#oauth-apps)
* [open](#open)
* [project](#project)
* [promote](#promote)
* [pull](#pull)
* [redeploy](#redeploy)
* [redirects](#redirects)
* [remove](#remove)
* [rollback](#rollback)
* [rolling-release](#rolling-release)
* [routes](#routes)
* [sandbox](#sandbox)
* [skills](#skills)
* [switch](#switch)
* [target](#target)
* [teams](#teams)
* [telemetry](#telemetry)
* [tokens](#tokens)
* [traces](#traces)
* [upgrade](#upgrade)
* [usage](#usage)
* [webhooks](#webhooks)
* [whoami](#whoami)