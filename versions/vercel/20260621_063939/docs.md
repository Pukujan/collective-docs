---
title: Docs Home — Ship anything with Vercel
source: vercel
url: https://vercel.com/docs
fetched: 2026-06-21T06:39:33.778264
---

# Docs Home — Ship anything with Vercel

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

# Ship anything with Vercel

Deploy your app on Vercel in three steps: install the CLI, add agent support if you use an AI coding agent, and deploy.[Get started guide](/docs/getting-started-with-vercel)[Get an API key](https://vercel.com/account/tokens)[API reference](/docs/rest-api)TypeScriptPythoncURLindex.ts```
`import { generateText } from 'ai';

const { text } = await generateText({
  model: 'anthropic/claude-opus-4.7',
  prompt: 'What is the capital of France?',
});`
```

index.py```
`import os
from openai import OpenAI

client = OpenAI(
  api_key=os.getenv('AI_GATEWAY_API_KEY'),
  base_url='https://ai-gateway.vercel.sh/v1'
)

response = client.chat.completions.create(
  model='openai/gpt-5.5',
  messages=[{'role': 'user', 'content': 'Why is the sky blue?'}]
)`
```

index.sh```
`curl -X POST "https://ai-gateway.vercel.sh/v1/chat/completions" \
-H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "model": "openai/gpt-5.5",
  "messages": [
    { "role": "user", "content": "Why is the sky blue?" }
  ]
}'`
```


Connect your [Git repository](/docs/git) to deploy on every push, with [automatic preview environments](/docs/deployments/environments#preview-environment-pre-production) for testing changes before production.


## p]:m-0" href="#build-with-ai">Build with AI[](#build-with-ai)


[### AI Gateway

Access hundreds of models through one endpoint with budgets, fallbacks, and monitoring.

](/docs/ai-gateway)[### Eve

Eve is a filesystem-first framework for building durable backend AI agents.

](/docs/eve)[### Agents

Build autonomous workflows and conversational interfaces with the AI SDK.

](/kb/guide/how-to-build-ai-agents-with-vercel-and-the-ai-sdk)[### Sandbox

Run untrusted code in secure, ephemeral execution environments.

](/docs/sandbox)
## p]:m-0" href="#build-your-applications">Build your applications[](#build-your-applications)


Use one or more of the following tools to build your application depending on your needs:


[### Next.js

Build full-stack applications with Next.js or any of our supported frameworks.

](/docs/frameworks/nextjs)[### Functions

API routes with Fluid compute, active CPU, and provisioned memory — perfect for AI workloads.

](/docs/functions)[### Routing Middleware

Customize your application's behavior with code that runs before a request is processed.

](/docs/routing-middleware)[### Incremental Static Regeneration

Automatically regenerate your pages on a schedule or when a request is made.

](/docs/incremental-static-regeneration)[### Image Optimization

Optimize your images for the web.

](/docs/image-optimization)[### Manage Environments

Local, preview, production, and custom environments.

](/docs/deployments/environments)
## p]:m-0" href="#use-vercel's-ai-infrastructure">Use Vercel's AI infrastructure[](#use-vercel's-ai-infrastructure)


Add intelligence to your applications with Vercel's AI-first infrastructure:


[### v0

Iterate on ideas with Vercel's AI-powered development assistant.

](https://v0.app/docs/introduction)[### AI SDK

Integrate language models with streaming and tool calling.

](/docs/ai-sdk)[### AI Gateway

Route to any AI provider with automatic failover.

](/docs/ai-gateway)[### MCP Servers

Create tools for AI agents to interact with your systems.

](/docs/mcp)[### Agent Resources

Access documentation for AI tools, MCP servers, agent skills, and more.

](/docs/agent-resources)[### Claim Deployments

Allow AI agents to deploy a project and let a human take over.

](/docs/deployments/claim-deployments)
## p]:m-0" href="#secure-your-applications">Secure your applications[](#secure-your-applications)


Secure your applications with the following tools:


[### Deployment Protection

Protect your applications from unauthorized access.

](/docs/deployment-protection)[### RBAC

Role-based access control for your applications.

](/docs/rbac)[### Configurable WAF

Customizable rules to protect against attacks, scrapers, and unwanted traffic.

](/docs/vercel-firewall/vercel-waf)[### Bot Management

Protect your applications from bots and automated traffic.

](/docs/bot-management)[### BotID

An invisible CAPTCHA that protects against sophisticated bots without challenges.

](/docs/botid)[### Platform DDoS Mitigation

Protect your applications from DDoS attacks.

](/docs/security/ddos-mitigation)
## p]:m-0" href="#collaborate-with-your-team">Collaborate with your team[](#collaborate-with-your-team)


Collaborate with your team using the following tools:


[### Toolbar

An in-browser toolbar to leave feedback, manage flags, preview drafts, and inspect performance.

](/docs/vercel-toolbar)[### Comments

Let teams and invited collaborators comment on your preview and production environments.

](/docs/comments)[### Draft Mode

View your unpublished headless CMS content on your site.

](/docs/draft-mode)
## p]:m-0" href="#deploy-and-scale">Deploy and scale[](#deploy-and-scale)


Vercel handles infrastructure automatically and provides these tools to help you deploy and scale:


[### Vercel Delivery Network

Fast, globally distributed execution.

](/docs/cdn)[### Rolling Releases

Roll out new deployments in increments.

](/docs/rolling-releases)[### Rollback Deployments

Roll back to a previous deployment for swift recovery from production incidents.

](/docs/instant-rollback)[### Observability Suite

Monitor performance and debug your AI workflows and apps.

](/docs/observability)
## p]:m-0" href="#guides-and-tutorials">Guides and tutorials[](#guides-and-tutorials)


Extend your knowledge with in-depth guides, videos, and tutorials on the [Vercel Knowledge Base](/kb):


[### AI

Build AI agents, integrate language models, and deploy AI-powered apps.

](/kb/ai)[### Backend

Server-side patterns, API routes, database connections, and compute.

](/kb/backend)[### Frontend

Performance optimization, rendering strategies, and framework best practices.

](/kb/frontend)[### Security

Protect your apps with authentication, firewall rules, and compliance guides.

](/kb/security)[### CDN

Cache content globally, route requests, and run compute close to your data.

](/kb/cdn)[### Integrations

Connect third-party tools, CMSs, and services to your Vercel project.

](/kb/integrations)[NextStart / Getting started](/docs/getting-started-with-vercel)Was this helpful?

input]:h-10 text-sm [&>input]:px-3 has-[:focus]:!shadow-[0_0_0_1px_var(--ds-gray-alpha-600),0px_0px_0px_4px_rgba(0,0,0,0.16)] dark-theme:has-[:focus]:!shadow-[0_0_0_1px_var(--ds-gray-alpha-600),0px_0px_0px_4px_rgba(255,255,255,0.24)] hover:shadow-[0_0_0_1px_var(--ds-gray-alpha-500)] hover:[&:has(input:disabled)]:shadow-[0_0_0_1px_var(--ds-gray-alpha-400)] hover:[&:has(textarea:disabled)]:shadow-[0_0_0_1px_var(--ds-gray-alpha-400)] w-full" data-geist-textarea-wrapper="">input]:h-10 text-sm [&>input]:px-3 has-[:focus]:!shadow-[0_0_0_1px_var(--ds-gray-alpha-600),0px_0px_0px_4px_rgba(0,0,0,0.16)] dark-theme:has-[:focus]:!shadow-[0_0_0_1px_var(--ds-gray-alpha-600),0px_0px_0px_4px_rgba(255,255,255,0.24)] hover:shadow-[0_0_0_1px_var(--ds-gray-alpha-500)] hover:[&:has(input:disabled)]:shadow-[0_0_0_1px_var(--ds-gray-alpha-400)] hover:[&:has(textarea:disabled)]:shadow-[0_0_0_1px_var(--ds-gray-alpha-400)] h-[100px]" spellCheck="false" placeholder="Your feedback..." id="feedback-textarea">supported.Send