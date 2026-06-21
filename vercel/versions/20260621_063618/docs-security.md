---
title: Security Documentation
source: vercel
url: https://vercel.com/docs/security
fetched: 2026-06-21T06:36:17.137293
---

# Security Documentation

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

Security & Compliance
* [Overview](/docs/security)
* [Security & Compliance Measures](/docs/security/compliance)
* [Shared Responsibility Model](/docs/security/shared-responsibility)
* [PCI DSS iframe Integration](/docs/security/pci-dss)
* [Audit Logs](/docs/audit-log)

Copy pageCopy page# p]:m-0">Vercel security overview

Copy pageCopy pageCloud-deployed web applications face constant security threats, with attackers launching millions of malicious attacks weekly. Your application, users, and business require robust security measures to stay protected.


A comprehensive security strategy requires active protection, robust policies, and compliance frameworks:


li::marker]:text-gray-500">
* svg]:inline-flex last:mb-0">[Security governance and policies](#governance-and-policies) ensure long-term organizational safety, maintain regulatory adherence, and establish consistent security practices across teams.

* svg]:inline-flex last:mb-0">A [Multi-layered protection](#multi-layered-protection) system provides active security against immediate threats and attacks.


## p]:m-0" href="#governance-and-policies">Governance and policies[](#governance-and-policies)


### p]:m-0" href="#compliance-measures">Compliance measures[](#compliance-measures)


Learn about the [protection and compliance measures](/docs/security/compliance) Vercel takes to ensure the security of your data, including DDoS mitigation, SOC2 Type 2 compliance, Data encryption, and more.


### p]:m-0" href="#shared-responsibility-model">Shared responsibility model[](#shared-responsibility-model)


A [shared responsibility model](/docs/security/shared-responsibility) is a framework designed to split tasks and obligations between two groups in cloud computing. The model divides duties to ensure security, maintenance, and service functionality.


### p]:m-0" href="#encryption">Encryption[](#encryption)


Out of the box, Vercel serves every deployment over an [HTTPS connection](/docs/security/encryption). Vercel automatically generates SSL certificates for these unique URLs free of charge.


## p]:m-0" href="#multi-layered-protection">Multi-layered protection[](#multi-layered-protection)


Understand how Vercel protects every incoming request with [multiple layers](/docs/security/firewall-concepts#how-vercel-secures-requests) of firewall and deployment protection.


### p]:m-0" href="#vercel-firewall">Vercel firewall[](#vercel-firewall)


The Vercel firewall helps to protect your applications and websites from malicious attacks and unauthorized access through:


li::marker]:text-gray-500">
* svg]:inline-flex last:mb-0">An enterprise-grade platform-wide firewall available for free for all customers with no configuration required that includes automatic [DDoS mitigation](/docs/security/ddos-mitigation) and protection against low quality traffic.

* svg]:inline-flex last:mb-0">A [Web Application Firewall (WAF)](/docs/security/vercel-waf) that supports custom rules, managed rulesets, and allows customers to challenge automated traffic. You can customize the WAF at the project level.

* svg]:inline-flex last:mb-0">[Observability](/docs/vercel-firewall/firewall-observability) into network traffic and firewall activity, including the access to firewall logs.


Last updated February 18, 2026[PreviousNetworking](/docs/networking)[NextSecurity & Compliance Measures](/docs/security/compliance)Was this helpful?

input]:h-10 text-sm [&>input]:px-3 has-[:focus]:!shadow-[0_0_0_1px_var(--ds-gray-alpha-600),0px_0px_0px_4px_rgba(0,0,0,0.16)] dark-theme:has-[:focus]:!shadow-[0_0_0_1px_var(--ds-gray-alpha-600),0px_0px_0px_4px_rgba(255,255,255,0.24)] hover:shadow-[0_0_0_1px_var(--ds-gray-alpha-500)] hover:[&:has(input:disabled)]:shadow-[0_0_0_1px_var(--ds-gray-alpha-400)] hover:[&:has(textarea:disabled)]:shadow-[0_0_0_1px_var(--ds-gray-alpha-400)] w-full" data-geist-textarea-wrapper="">input]:h-10 text-sm [&>input]:px-3 has-[:focus]:!shadow-[0_0_0_1px_var(--ds-gray-alpha-600),0px_0px_0px_4px_rgba(0,0,0,0.16)] dark-theme:has-[:focus]:!shadow-[0_0_0_1px_var(--ds-gray-alpha-600),0px_0px_0px_4px_rgba(255,255,255,0.24)] hover:shadow-[0_0_0_1px_var(--ds-gray-alpha-500)] hover:[&:has(input:disabled)]:shadow-[0_0_0_1px_var(--ds-gray-alpha-400)] hover:[&:has(textarea:disabled)]:shadow-[0_0_0_1px_var(--ds-gray-alpha-400)] h-[100px]" spellCheck="false" placeholder="Your feedback..." id="feedback-textarea">supported.Send## On this page


* [Governance and policies](#governance-and-policies)
* [Compliance measures](#compliance-measures)
* [Shared responsibility model](#shared-responsibility-model)
* [Encryption](#encryption)
* [Multi-layered protection](#multi-layered-protection)
* [Vercel firewall](#vercel-firewall)