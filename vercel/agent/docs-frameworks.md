# Framework Documentation
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
Frameworks
* [Overview](/docs/frameworks)
* [All Frameworks](/docs/frameworks/more-frameworks)
Copy pageCopy page# p]:m-0">Frameworks on Vercel
Copy pageCopy pageVercel has first-class support for [a wide range of the most popular frameworks](/docs/frameworks/more-frameworks). You can build and deploy using frontend, backend, and full-stack frameworks ranging from SvelteKit to Nitro, often without any upfront configuration.
Learn how to [get started with Vercel](/docs/getting-started-with-vercel) or clone one of our example repos to your favorite git provider and deploy it on Vercel using one of the templates below:
Get started in minutes
## Deploy a Template
[View All Templates](https://vercel.com/templates/starter)[![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F1aHobcZ8H6WY48u5CMXlOe%2F13f7ae605e457bb132a12cf7db323f43%2Fnextjs-template_1.png&w=3840&q=75)Next.js Boilerplate
Get started with Next.js and React in seconds.
](https://vercel.com/templates/next.js/nextjs-boilerplate)Open in v0[![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F5WIYQtnSEfZKYFB9kvsR0w%2F974bee31f87aa376a54dccdb0713629d%2FCleanShot_2022-05-23_at_22.13.20_2x.png&w=3840&q=75)SvelteKit Boilerplate
A SvelteKit app including nested routes, layouts, and page endpoints.
](https://vercel.com/templates/svelte/sveltekit-boilerplate)Open in v0[View All Templates](https://vercel.com/templates/starter)
Vercel deployments can [integrate with your git provider](/docs/git) to [generate preview URLs](/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your project.
Deploying on Vercel with one of our [supported frameworks](/docs/frameworks/more-frameworks) gives you access to many features, such as:
li::marker]:text-gray-500">
* svg]:inline-flex last:mb-0">[Vercel Functions](/docs/functions) enable developers to write functions that scale based on traffic demands, preventing failures during peak hours and reducing costs during low activity.
* svg]:inline-flex last:mb-0">[Middleware](/docs/routing-middleware) is code that executes before a request is processed on a site, enabling you to modify the response. Because it runs before the cache, Middleware is an effective way to personalize statically generated content.
* svg]:inline-flex last:mb-0">[Multi-runtime Support](/docs/functions/runtimes) allows the use of various runtimes for your functions, each with unique libraries, APIs, and features tailored to different technical requirements.
* svg]:inline-flex last:mb-0">[Incremental Static Regeneration](/docs/incremental-static-regeneration) enables content updates without redeployment. Vercel caches the page to serve it statically and rebuilds it on a specified interval.
* svg]:inline-flex last:mb-0">[Speed Insights](/docs/speed-insights) provide data on your project's Core Web Vitals performance in the Vercel dashboard, helping you improve loading speed, responsiveness, and visual stability.
* svg]:inline-flex last:mb-0">[Analytics](/docs/analytics) offer detailed insights into your website's performance over time, including metrics like top pages, top referrers, and user demographics.
* svg]:inline-flex last:mb-0">[Skew Protection](/docs/skew-protection) uses version locking to ensure that the client and server use the same version of your application, preventing version skew and related errors.
## p]:m-0" href="#frameworks-infrastructure-support-matrix">Frameworks infrastructure support matrix[](#frameworks-infrastructure-support-matrix)
The following table shows which features are supported by each framework on Vercel. The framework list represents the most popular frameworks deployed on Vercel.
SupportedNot Supported* Not Applicable
[TABLE]
Framework feature matrix | Feature  Next.js  SvelteKit  Nuxt  TanStack  Astro  Remix  Vite  CRA  |
[/TABLE]
No rows displayed.
## p]:m-0" href="#build-output-api">Build Output API[](#build-output-api)
The [Build Output API](/docs/build-output-api/v3) is a file-system-based specification for a directory structure that produces a Vercel deployment. It is primarily targeted at framework authors who want to integrate their frameworks with Vercel's platform features. By implementing this directory structure as the output of their build command, framework authors can utilize all Vercel platform features, such as Vercel Functions, Routing, and Caching.
If you are not using a framework, you can still use these features by manually creating and populating the `.vercel/output` directory according to this specification. Complete examples of Build Output API directories can be found in [vercel/examples](https://github.com/vercel/examples/tree/main/build-output-api), and you can read our [blog post](/blog/build-your-own-web-framework) on using the Build Output API to build your own framework with Vercel.
## p]:m-0" href="#more-resources">More resources[](#more-resources)
Learn more about deploying your preferred framework on Vercel with the following resources:
li::marker]:text-gray-500">
svg]:inline-flex last:mb-0">[See a full list of supported frameworks](/docs/frameworks/more-frameworks)
* svg]:inline-flex last:mb-0">[Explore our template marketplace](/templates)
* svg]:inline-flex last:mb-0">[Learn about our deployment features](/docs/deployments)
* [Frameworks infrastructure support matrix](#frameworks-infrastructure-support-matrix)
* [Build Output API](#build-output-api)
* [More resources](#more-resources)