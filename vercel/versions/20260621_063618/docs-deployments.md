---
title: Deploying to Vercel
source: vercel
url: https://vercel.com/docs/deployments
fetched: 2026-06-21T06:36:14.680660
---

# Deploying to Vercel

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

Deployments
* [Overview](/docs/deployments)
* [Environments](/docs/deployments/environments)
* [Generated URLs](/docs/deployments/generated-urls)
* [Managing Deployments](/docs/deployments/managing-deployments)
* [Promoting Deployments](/docs/deployments/promoting-a-deployment)
* [Troubleshoot Build Errors](/docs/deployments/troubleshoot-a-build)
* [Accessing Build Logs](/docs/deployments/logs)
* [Claim Deployments](/docs/deployments/claim-deployments)
* [Inspect OG Metadata](/docs/deployments/og-preview)
* [Preview Deployment Suffix](/docs/deployments/preview-deployment-suffix)
* [Promote Preview to Production](/docs/deployments/promote-preview-to-production)
* [Rollback Production](/docs/deployments/rollback-production-deployment)
* [Sharing a Preview Deployment](/docs/deployments/sharing-deployments)
* [Troubleshoot Project Collaboration](/docs/deployments/troubleshoot-project-collaboration)
* [Deploy Hooks](/docs/deploy-hooks)
* [Deployment Checks](/docs/deployment-checks)
* [Skew Protection](/docs/skew-protection)
* [Deployment Retention](/docs/deployment-retention)

Copy pageCopy pageCopy pageCopy page# Deploying to Vercel

Every time your project builds successfully, Vercel creates a deployment with its own URL. Push code, run a CLI command, call the API, or drag a folder into your browser — you choose how to ship.[Connect Git](/docs/git)[Use the CLI](/docs/cli)Terminal```
`npm i -g vercel
vercel --prod`
```


A deployment on Vercel is the result of a successful build of your project. Each time you deploy, Vercel generates a unique URL so you and your team can preview changes in a live [environment](/docs/deployments/environments).


Vercel supports multiple ways to create a deployment:


li::marker]:text-gray-500">
* svg]:inline-flex last:mb-0">[Git](#git)

* svg]:inline-flex last:mb-0">[Vercel Drop](#vercel-drop)

* svg]:inline-flex last:mb-0">[Vercel CLI](#vercel-cli)

* svg]:inline-flex last:mb-0">[Deploy Hooks](#deploy-hooks)

* svg]:inline-flex last:mb-0">[Vercel REST API](#vercel-rest-api)


## p]:m-0" href="#deployment-methods">Deployment Methods[](#deployment-methods)


### p]:m-0" href="#git">Git[](#git)


The most common way to create a deployment is by pushing code to a connected [Git repository](/docs/git). When you [import a Git repository to Vercel](/docs/git#deploying-a-git-repository), each commit or pull request (on supported Git providers) automatically triggers a new deployment.


Vercel supports the following providers:


li::marker]:text-gray-500">
* svg]:inline-flex last:mb-0">[GitHub](/docs/git/vercel-for-github)

* svg]:inline-flex last:mb-0">[GitLab](/docs/git/vercel-for-gitlab)

* svg]:inline-flex last:mb-0">[Bitbucket](/docs/git/vercel-for-bitbucket)

* svg]:inline-flex last:mb-0">[Azure DevOps](/docs/git/vercel-for-azure-pipelines)


You can also [create deployments from a Git reference](/docs/git#creating-a-deployment-from-a-git-reference) using the Vercel Dashboard if you need to deploy specific commits or branches manually.


### p]:m-0" href="#vercel-drop">Vercel Drop[](#vercel-drop)


[Vercel Drop](/docs/drop) lets you deploy a file or folder by dragging it into your browser. You don't need Git, the CLI, or any local setup.


* svg]:inline-flex last:mb-0">Go to [vercel.com/drop](/drop).

* svg]:inline-flex last:mb-0">Drag a project folder onto the page.

* svg]:inline-flex last:mb-0">Choose a team and project name, then select Deploy.


Vercel detects your framework and builds it, or deploys your files as-is when there's no framework. Vercel Drop is useful for static sites, build output, and prototypes. For the full walkthrough, see [Deploying with Vercel Drop](/docs/drop).


### p]:m-0" href="#vercel-cli">Vercel CLI[](#vercel-cli)


You can deploy your Projects directly from the command line using [Vercel CLI](/docs/cli). This method works whether your project is connected to Git or not.


* svg]:inline-flex last:mb-0">Install Vercel CLI:


Terminal```
`npm i -g vercel`
```


* svg]:inline-flex last:mb-0">Initial Deployment:


In your project's root directory, run:


```
`vercel --prod`
```


This links your local directory to your Vercel Project and creates a [Production Deployment](/docs/deployments/environments#production-environment). A `.vercel` directory is added to store Project and Organization IDs.


Vercel CLI can also integrate with custom CI/CD workflows or third-party pipelines. Learn more about the different [environments on Vercel](/docs/deployments/environments).


### p]:m-0" href="#deploy-hooks">Deploy Hooks[](#deploy-hooks)


[Deploy Hooks](/docs/deploy-hooks) let you trigger deployments with a unique URL. You must have a connected Git repository to use this feature, but the deployment doesn't require a new commit.


* svg]:inline-flex last:mb-0">From your Project settings, create a Deploy Hook

* svg]:inline-flex last:mb-0">Vercel generates a unique URL for each Project

* svg]:inline-flex last:mb-0">Make an HTTP `GET` or `POST` request to this URL to trigger the deployment


Refer to the [Deploy Hooks documentation](/docs/deploy-hooks) for more information.


### p]:m-0" href="#vercel-rest-api">Vercel REST API[](#vercel-rest-api)


The [Vercel REST API](/docs/rest-api) lets you create deployments by making an HTTP `POST` request to the deployment endpoint. In this workflow:


* svg]:inline-flex last:mb-0">Generate a SHA for each file you want to deploy

* svg]:inline-flex last:mb-0">Upload those files to Vercel

* svg]:inline-flex last:mb-0">Send a request to create a new deployment with those file references


This method is especially useful for custom workflows, multi-tenant applications, or integrating with third-party services not officially supported by Vercel. For more details, see the [API reference](/docs/rest-api/reference/endpoints/deployments/create-a-new-deployment) and [How do I generate an SHA for uploading a file](/kb/guide/how-do-i-generate-an-sha-for-uploading-a-file-to-the-vercel-api).


## p]:m-0" href="#accessing-deployments">Accessing Deployments[](#accessing-deployments)


Vercel provides three default environments: Local, Preview, and Production.


* svg]:inline-flex last:mb-0">Local Development: developing and testing code changes on your local machine

* svg]:inline-flex last:mb-0">Preview: deploying for further testing, QA, or collaboration without impacting your live site

* svg]:inline-flex last:mb-0">Production: deploying the final changes to your user-facing site with the production domain


Learn more about [environments](/docs/deployments/environments).


## p]:m-0" href="#using-the-dashboard">Using the Dashboard[](#using-the-dashboard)


Vercel’s dashboard provides a centralized way to view, manage, and gain insights into your deployments.


### p]:m-0" href="#resources-tab-and-deployment-summary">Resources Tab and Deployment Summary[](#resources-tab-and-deployment-summary)


li::marker]:text-gray-500">
* svg]:inline-flex last:mb-0">Middleware: Any configured [matchers](/docs/routing-middleware/api#match-paths-based-on-custom-matcher-config).

* svg]:inline-flex last:mb-0">Static Assets: Files (HTML, CSS, JS) and their sizes.

* svg]:inline-flex last:mb-0">Functions: The type, runtime, size, and regions.


![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeployment-resources-page-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeployment-resources-page-dark.png&w=3840&q=75)Example of a deployment resources page with a search applied.
You can also see a summary of these resources by expanding the Deployment Summary section on a Deployment Details page. To visit the Deployment Details page for a deployment, select it from your Project → Deployments page.


![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeploy-outputs-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeploy-outputs-dark.png&w=3840&q=75)Example of an open deployment summary.
You’ll also see your build time, detected framework, and any relevant logs or errors.


### p]:m-0" href="#project-overview">Project Overview[](#project-overview)


On your Project Overview page, you can see the latest production deployment, including the generated URL and commit details, and deployment logs for debugging.


### p]:m-0" href="#managing-deployments">Managing Deployments[](#managing-deployments)


li::marker]:text-gray-500">
* svg]:inline-flex last:mb-0">Redeploy: Re-run the build for a specific commit or configuration.

* svg]:inline-flex last:mb-0">Inspect: View logs and build outputs.

* svg]:inline-flex last:mb-0">Assign a Custom Domain: Point custom domains to any deployment.

* svg]:inline-flex last:mb-0">Promote to Production: Convert a preview deployment to production (if needed).


For more information on interacting with your deployments, see [Managing Deployments](/docs/deployments/managing-deployments).


## p]:m-0" href="#cli-workflows">CLI workflows[](#cli-workflows)


For step-by-step workflows using the Vercel CLI to manage deployments, see:


li::marker]:text-gray-500">
* svg]:inline-flex last:mb-0">[Rolling back a production deployment](/docs/deployments/rollback-production-deployment)

* svg]:inline-flex last:mb-0">[Deploying a project from the CLI](/docs/projects/deploy-from-cli)


## p]:m-0" href="#explore-deployments">Explore deployments[](#explore-deployments)


[### Vercel Drop

Deploy a folder by dragging it into your browser. No Git or CLI required.

](/docs/drop)[### Deploy from Git

Connect GitHub, GitLab, Bitbucket, or Azure DevOps for automatic deployments.

](/docs/git)[### Deploy with the CLI

Deploy from your terminal or CI/CD pipeline.

](/docs/cli)[### Deploy Hooks

Trigger deployments with a unique URL.

](/docs/deploy-hooks)[### Vercel REST API

Create deployments programmatically via HTTP.

](/docs/rest-api)[### Environments

Understand local, preview, and production environments.

](/docs/deployments/environments)[### Managing deployments

Redeploy, inspect, assign domains, and promote to production.

](/docs/deployments/managing-deployments)[### Rolling back a production deployment

Revert to a previous production deployment safely.

](/docs/deployments/rollback-production-deployment)[### Deploy from the CLI

Deploy a project end-to-end using Vercel CLI.

](/docs/projects/deploy-from-cli)[PreviousBuilds](/docs/builds)[NextEnvironments](/docs/deployments/environments)Was this helpful?

input]:h-10 text-sm [&>input]:px-3 has-[:focus]:!shadow-[0_0_0_1px_var(--ds-gray-alpha-600),0px_0px_0px_4px_rgba(0,0,0,0.16)] dark-theme:has-[:focus]:!shadow-[0_0_0_1px_var(--ds-gray-alpha-600),0px_0px_0px_4px_rgba(255,255,255,0.24)] hover:shadow-[0_0_0_1px_var(--ds-gray-alpha-500)] hover:[&:has(input:disabled)]:shadow-[0_0_0_1px_var(--ds-gray-alpha-400)] hover:[&:has(textarea:disabled)]:shadow-[0_0_0_1px_var(--ds-gray-alpha-400)] w-full" data-geist-textarea-wrapper="">input]:h-10 text-sm [&>input]:px-3 has-[:focus]:!shadow-[0_0_0_1px_var(--ds-gray-alpha-600),0px_0px_0px_4px_rgba(0,0,0,0.16)] dark-theme:has-[:focus]:!shadow-[0_0_0_1px_var(--ds-gray-alpha-600),0px_0px_0px_4px_rgba(255,255,255,0.24)] hover:shadow-[0_0_0_1px_var(--ds-gray-alpha-500)] hover:[&:has(input:disabled)]:shadow-[0_0_0_1px_var(--ds-gray-alpha-400)] hover:[&:has(textarea:disabled)]:shadow-[0_0_0_1px_var(--ds-gray-alpha-400)] h-[100px]" spellCheck="false" placeholder="Your feedback..." id="feedback-textarea">supported.Send## On this page


* [Deployment Methods](#deployment-methods)
* [Git](#git)
* [Vercel Drop](#vercel-drop)
* [Vercel CLI](#vercel-cli)
* [Deploy Hooks](#deploy-hooks)
* [Vercel REST API](#vercel-rest-api)
* [Accessing Deployments](#accessing-deployments)
* [Using the Dashboard](#using-the-dashboard)
* [Resources Tab and Deployment Summary](#resources-tab-and-deployment-summary)
* [Project Overview](#project-overview)
* [Managing Deployments](#managing-deployments)
* [CLI workflows](#cli-workflows)
* [Explore deployments](#explore-deployments)