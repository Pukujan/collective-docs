# Vercel REST API Reference
[Vercel REST API](/docs)[Overview](/docs/rest-api)[Errors](/docs/rest-api/errors)
* Access-groups
* Aliases
* Api-observability
* Artifacts
* Authentication
* Billing
* Bulk-redirects
* Certs
* Checks-v2
* Connect
* Deployments
* DNS
* Domains
* Domains-registrar
* Drains
* Edge-cache
* Edge-config
* Environment
* Feature-flags
* Integrations
* Logs
* Marketplace
* Microfrontends
* Networking
* Project-routes
* Projectmembers
* Projects
* Rolling-release
* Sandboxes
* Security
* Static-ips
* Teams
* User
* Webhooks
APIs & SDKsVercel REST API# p]:m-0" href="#using-the-rest-api">Using the REST API[](#using-the-rest-api)
Interact programmatically with your Vercel account using the SDK or direct HTTP requests. You can deploy new versions of web applications, manage custom domains, retrieve information about deployments, and manage secrets and environment variables for projects.
The API supports any programming language or framework that can send HTTP requests.
## p]:m-0" href="#api-basics">API basics[](#api-basics)
The API is exposed as an HTTP/1 and HTTP/2 service over SSL. All endpoints live under the URL `https://api.vercel.com` and follow the REST architecture.
## p]:m-0" href="#authentication">Authentication[](#authentication)
Vercel Access Tokens are required to authenticate and use the Vercel API. Include the token in the `Authorization` header:
`Authorization: Bearer `Create and manage Access Tokens in your [account settings](https://vercel.com/account/tokens).
## p]:m-0" href="#accessing-team-resources">Accessing team resources[](#accessing-team-resources)
By default, you can access resources in your personal account. To access resources owned by a team, append the Team ID as a query string:
`https://api.vercel.com/v6/deployments?teamId=[teamID]`## p]:m-0" href="#rate-limits">Rate limits[](#rate-limits)
The API limits the number of calls you can make over a period of time. Rate limits are specified via response headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset`. See the [limits documentation](/docs/limits#rate-limits) for details.
## p]:m-0" href="#endpoints">Endpoints[](#endpoints)
Browse all available REST API endpoints grouped by category.
* [API basics](#api-basics)
* [Authentication](#authentication)
* [Accessing team resources](#accessing-team-resources)
* [Rate limits](#rate-limits)
* [Endpoints](#endpoints)