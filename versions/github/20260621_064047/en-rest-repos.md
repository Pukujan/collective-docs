---
title: REST API — Repos
source: github
url: https://docs.github.com/en/rest/repos
fetched: 2026-06-21T06:40:40.206005
---

# REST API — Repos

The REST API is now versioned. For more information, see "[About API versioning](/rest/overview/api-versions)."
* [REST API](/en/rest)/
* [Repositories](/en/rest/repos)

# REST API endpoints for repositories

Use the REST API to create, manage and control the workflow of public and private GitHub repositories.


* [REST API endpoints for repositories](/en/rest/repos/repos)
[List organization repositories](/en/rest/repos/repos#list-organization-repositories)
* [Create an organization repository](/en/rest/repos/repos#create-an-organization-repository)
* [Get a repository](/en/rest/repos/repos#get-a-repository)
* [Update a repository](/en/rest/repos/repos#update-a-repository)
* [Delete a repository](/en/rest/repos/repos#delete-a-repository)
* [List repository activities](/en/rest/repos/repos#list-repository-activities)
* [Check if Dependabot security updates are enabled for a repository](/en/rest/repos/repos#check-if-dependabot-security-updates-are-enabled-for-a-repository)
* [Enable Dependabot security updates](/en/rest/repos/repos#enable-dependabot-security-updates)
* [Disable Dependabot security updates](/en/rest/repos/repos#disable-dependabot-security-updates)
* [List CODEOWNERS errors](/en/rest/repos/repos#list-codeowners-errors)
* [List repository contributors](/en/rest/repos/repos#list-repository-contributors)
* [Create a repository dispatch event](/en/rest/repos/repos#create-a-repository-dispatch-event)
* [Get the hash algorithm for a repository](/en/rest/repos/repos#get-the-hash-algorithm-for-a-repository)
* [Check if immutable releases are enabled for a repository](/en/rest/repos/repos#check-if-immutable-releases-are-enabled-for-a-repository)
* [Enable immutable releases](/en/rest/repos/repos#enable-immutable-releases)
* [Disable immutable releases](/en/rest/repos/repos#disable-immutable-releases)
* [List repository languages](/en/rest/repos/repos#list-repository-languages)
* [Check if private vulnerability reporting is enabled for a repository](/en/rest/repos/repos#check-if-private-vulnerability-reporting-is-enabled-for-a-repository)
* [Enable private vulnerability reporting for a repository](/en/rest/repos/repos#enable-private-vulnerability-reporting-for-a-repository)
* [Disable private vulnerability reporting for a repository](/en/rest/repos/repos#disable-private-vulnerability-reporting-for-a-repository)
* [List repository tags](/en/rest/repos/repos#list-repository-tags)
* [List repository teams](/en/rest/repos/repos#list-repository-teams)
* [Get all repository topics](/en/rest/repos/repos#get-all-repository-topics)
* [Replace all repository topics](/en/rest/repos/repos#replace-all-repository-topics)
* [Transfer a repository](/en/rest/repos/repos#transfer-a-repository)
* [Check if vulnerability alerts are enabled for a repository](/en/rest/repos/repos#check-if-vulnerability-alerts-are-enabled-for-a-repository)
* [Enable vulnerability alerts](/en/rest/repos/repos#enable-vulnerability-alerts)
* [Disable vulnerability alerts](/en/rest/repos/repos#disable-vulnerability-alerts)
* [Create a repository using a template](/en/rest/repos/repos#create-a-repository-using-a-template)
* [List public repositories](/en/rest/repos/repos#list-public-repositories)
* [List repositories for the authenticated user](/en/rest/repos/repos#list-repositories-for-the-authenticated-user)
* [Create a repository for the authenticated user](/en/rest/repos/repos#create-a-repository-for-the-authenticated-user)
* [List repositories for a user](/en/rest/repos/repos#list-repositories-for-a-user)

* [REST API endpoints for repository attestations](/en/rest/repos/attestations)
[Create an attestation](/en/rest/repos/attestations#create-an-attestation)
* [List attestations](/en/rest/repos/attestations#list-attestations)

* [REST API endpoints for repository autolinks](/en/rest/repos/autolinks)
[Get all autolinks of a repository](/en/rest/repos/autolinks#get-all-autolinks-of-a-repository)
* [Create an autolink reference for a repository](/en/rest/repos/autolinks#create-an-autolink-reference-for-a-repository)
* [Get an autolink reference of a repository](/en/rest/repos/autolinks#get-an-autolink-reference-of-a-repository)
* [Delete an autolink reference from a repository](/en/rest/repos/autolinks#delete-an-autolink-reference-from-a-repository)

* [REST API endpoints for repository contents](/en/rest/repos/contents)
[Get repository content](/en/rest/repos/contents#get-repository-content)
* [Create or update file contents](/en/rest/repos/contents#create-or-update-file-contents)
* [Delete a file](/en/rest/repos/contents#delete-a-file)
* [Get a repository README](/en/rest/repos/contents#get-a-repository-readme)
* [Get a repository README for a directory](/en/rest/repos/contents#get-a-repository-readme-for-a-directory)
* [Download a repository archive (tar)](/en/rest/repos/contents#download-a-repository-archive-tar)
* [Download a repository archive (zip)](/en/rest/repos/contents#download-a-repository-archive-zip)

* [REST API endpoints for custom properties](/en/rest/repos/custom-properties)
[Get all custom property values for a repository](/en/rest/repos/custom-properties#get-all-custom-property-values-for-a-repository)
* [Create or update custom property values for a repository](/en/rest/repos/custom-properties#create-or-update-custom-property-values-for-a-repository)

* [REST API endpoints for forks](/en/rest/repos/forks)
[List forks](/en/rest/repos/forks#list-forks)
* [Create a fork](/en/rest/repos/forks#create-a-fork)

* [REST API endpoints for issue types](/en/rest/repos/issue-types)
[List issue types for a repository](/en/rest/repos/issue-types#list-issue-types-for-a-repository)

* [REST API endpoints for rule suites](/en/rest/repos/rule-suites)
[List repository rule suites](/en/rest/repos/rule-suites#list-repository-rule-suites)
* [Get a repository rule suite](/en/rest/repos/rule-suites#get-a-repository-rule-suite)

* [REST API endpoints for rules](/en/rest/repos/rules)
[Get rules for a branch](/en/rest/repos/rules#get-rules-for-a-branch)
* [Get all repository rulesets](/en/rest/repos/rules#get-all-repository-rulesets)
* [Create a repository ruleset](/en/rest/repos/rules#create-a-repository-ruleset)
* [Get a repository ruleset](/en/rest/repos/rules#get-a-repository-ruleset)
* [Update a repository ruleset](/en/rest/repos/rules#update-a-repository-ruleset)
* [Delete a repository ruleset](/en/rest/repos/rules#delete-a-repository-ruleset)
* [Get repository ruleset history](/en/rest/repos/rules#get-repository-ruleset-history)
* [Get repository ruleset version](/en/rest/repos/rules#get-repository-ruleset-version)

* [REST API endpoints for repository webhooks](/en/rest/repos/webhooks)
[List repository webhooks](/en/rest/repos/webhooks#list-repository-webhooks)
* [Create a repository webhook](/en/rest/repos/webhooks#create-a-repository-webhook)
* [Get a repository webhook](/en/rest/repos/webhooks#get-a-repository-webhook)
* [Update a repository webhook](/en/rest/repos/webhooks#update-a-repository-webhook)
* [Delete a repository webhook](/en/rest/repos/webhooks#delete-a-repository-webhook)
* [Get a webhook configuration for a repository](/en/rest/repos/webhooks#get-a-webhook-configuration-for-a-repository)
* [Update a webhook configuration for a repository](/en/rest/repos/webhooks#update-a-webhook-configuration-for-a-repository)
* [List deliveries for a repository webhook](/en/rest/repos/webhooks#list-deliveries-for-a-repository-webhook)
* [Get a delivery for a repository webhook](/en/rest/repos/webhooks#get-a-delivery-for-a-repository-webhook)
* [Redeliver a delivery for a repository webhook](/en/rest/repos/webhooks#redeliver-a-delivery-for-a-repository-webhook)
* [Ping a repository webhook](/en/rest/repos/webhooks#ping-a-repository-webhook)
* [Test the push repository webhook](/en/rest/repos/webhooks#test-the-push-repository-webhook)