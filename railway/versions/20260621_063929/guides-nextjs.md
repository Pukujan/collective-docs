---
title: Guide — Next.js
source: railway
url: https://docs.railway.com/guides/nextjs
fetched: 2026-06-21T06:39:28.028984
---

# Guide — Next.js

# Deploy a Next.js App with Postgres

deploymentfrontendnextjsfullstackOn this page[Next.js](https://nextjs.org) is a React framework for building full-stack web applications. It handles server-side rendering, static generation, API routes, and routing.


This guide covers how to deploy a Next.js app to Railway and connect it to a Postgres database:


* [One-click deploy from a template](#one-click-deploy-from-a-template).

* [From a GitHub repository](#deploy-from-a-github-repo).

* [Using the CLI](#deploy-from-the-cli).

* [Using a Dockerfile](#use-a-dockerfile).

* [Add a Postgres database](#add-a-postgres-database).


## [Create a Next.js App](#create-a-nextjs-app)


**Note:** If you already have a Next.js app locally or on GitHub, you can skip this step and go straight to [Deploy the Next.js App to Railway](#deploy-the-nextjs-app-to-railway).


To create a new Next.js app, ensure that you have [Node](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs) installed on your machine.


Run the following command in your terminal to create a new Next.js app:


Follow the prompts to configure your app. The defaults work well for most projects.


### [Run the Next.js App locally](#run-the-nextjs-app-locally)


`cd` into the directory and start the development server:


Open your browser and go to `http://localhost:3000` to see your app.


## [Deploy the Next.js App to Railway](#deploy-the-nextjs-app-to-railway)


Railway offers multiple ways to deploy your Next.js app, depending on your setup and preference.


### [One-Click Deploy from a Template](#one-click-deploy-from-a-template)


If you're looking for the fastest way to get started, the one-click deploy option is ideal.


Click the button below to begin:


[![](https://railway.com/button.svg)](https://railway.com/new/template/HRZqTF)


We highly recommend that [you eject from the template after deployment](/guides/deploy#eject-from-template-repository) to create a copy of the repo on your GitHub account.


**Note:** You can also choose from a [variety of Next.js app templates](https://railway.com/templates?q=nextjs) created by the community.


### [Deploy from the CLI](#deploy-from-the-cli)


*
**Install the Railway CLI**:


[Install the CLI](/cli#installing-the-cli) and [authenticate it](/cli#authenticating-with-the-cli) using your Railway account.


*
**Initialize a Railway Project**:


Run the command below in your Next.js app directory.


* Follow the prompts to name your project.

* After the project is created, click the provided link to view it in your browser.


*
**Configure for Standalone Output**:


Next.js needs to produce a standalone build for self-hosted deployment. Add the `output` option to your `next.config.ts` (or `next.config.js`) file:


**next.config.ts**


Then update the start script in `package.json` to serve the standalone server:


**package.json**


**Note:** Railway uses [Railpack](/builds/railpack) (or [Nixpacks](/builds/nixpacks)) to build and deploy your code with zero configuration. The Node provider will pick up the start script in `package.json` and use it to serve the app.


*
**Deploy the Application**:


Use the command below to deploy your app:


* This command will scan, compress and upload your app's files to Railway. You'll see real-time deployment logs in your terminal.

* Once the deployment completes, go to **View logs** to check if the service is running successfully.


*
**Set Up a Public URL**:


* Click [Generate Domain](/networking/public-networking#railway-provided-domain) to create a public URL for your app.


### [Deploy from a GitHub Repo](#deploy-from-a-github-repo)


To deploy a Next.js app to Railway directly from GitHub, follow the steps below:


* **Create a New Project on Railway**:


Go to [Railway](https://railway.com/new) to create a new project.


* **Configure for Standalone Output**:


Follow [step 3 mentioned in the CLI guide](#deploy-from-the-cli) to set `output: "standalone"` and update the start script.


* **Deploy from GitHub**:


Select **Deploy from GitHub repo** and choose your repository.


If your Railway account isn't linked to GitHub yet, you'll be prompted to do so.


* **Deploy the App**:


Click **Deploy** to start the deployment process.

* Once deployed, a Railway [service](/services) will be created for your app, but it won't be publicly accessible by default.


* **Verify the Deployment**:


Once the deployment completes, go to **View logs** to check if the server is running successfully.


* **Set Up a Public URL**:


* Click [Generate Domain](/networking/public-networking#railway-provided-domain) to create a public URL for your app.


### [Use a Dockerfile](#use-a-dockerfile)


*
Create a `Dockerfile` in your Next.js app's root directory.


*
Add the content below to the `Dockerfile`:


**Note:** This Dockerfile requires `output: "standalone"` in your `next.config.ts` as described in [step 3 of the CLI guide](#deploy-from-the-cli).


*
Either deploy via the CLI or from GitHub.


Railway automatically detects the `Dockerfile`, [and uses it to build and deploy the app.](/builds/dockerfiles)


**Note:** Railway also supports [deployment from public and private Docker images](/builds/private-registries).


## [Add a Postgres database](#add-a-postgres-database)


Next.js apps that use API routes or server actions often need a database. Railway lets you add Postgres to your project in a few clicks.


### [Provision the database](#provision-the-database)


* Open your project on Railway.

* Click **+ New** on the project canvas and select **Database** → **PostgreSQL**.

* Railway provisions the database and exposes connection variables (`DATABASE_URL`, `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, `PGDATABASE`) in the database service.


### [Connect your Next.js service to Postgres](#connect-your-nextjs-service-to-postgres)


* Click on your Next.js service in the project canvas.

* Go to the **Variables** tab.

* Click **Add Reference Variable** and select `DATABASE_URL` from the Postgres service.


This creates a [reference variable](/variables#referencing-another-services-variable) that stays in sync if the database credentials change.


* Redeploy the service for the new variable to take effect.


Your app can now read `DATABASE_URL` from `process.env` to connect to Postgres. Most ORMs and query builders (Prisma, Drizzle, Knex) use this variable automatically.


### [Run migrations with a pre-deploy command](#run-migrations-with-a-pre-deploy-command)


If your project uses an ORM that requires migrations (for example, Prisma or Drizzle), configure a [pre-deploy command](/deployments/pre-deploy-command) so migrations run before the new version starts serving traffic.


* In your Next.js service on Railway, go to **Settings** → **Deploy** → **Pre-deploy Command**.

* Set the command to your migration script. For example:


**Prisma**: `npx prisma migrate deploy`

* **Drizzle**: `npx drizzle-kit migrate`


* Railway runs this command in a separate container with access to your service's environment variables, including `DATABASE_URL`.


**Note:** The pre-deploy container does not have access to volumes. If your migration process requires file system state beyond what is in the build image, handle that in the build step instead.


## [Next steps](#next-steps)


Explore these resources to learn how you can maximize your experience with Railway:


* [Choose between SSR, SSG, and ISR](/guides/ssr-ssg-isr) - Pick the right rendering strategy.

* [Manage environment variables](/guides/frontend-environment-variables) - Handle `NEXT_PUBLIC_` prefixed variables.

* [Deploy a full-stack Next.js app](/guides/fullstack-nextjs) - Add Postgres, workers, and file uploads.

* [PostgreSQL on Railway](/databases/postgresql)

* [Monitor your app](/observability)

* [Running a Cron Job](/cron-jobs)

* [Pre-deploy Command](/deployments/pre-deploy-command)


### On this page

[Create a Next.js App](#create-a-nextjs-app)[Run the Next.js App locally](#run-the-nextjs-app-locally)[Deploy the Next.js App to Railway](#deploy-the-nextjs-app-to-railway)[One-Click Deploy from a Template](#one-click-deploy-from-a-template)[Deploy from the CLI](#deploy-from-the-cli)[Deploy from a GitHub Repo](#deploy-from-a-github-repo)[Use a Dockerfile](#use-a-dockerfile)[Add a Postgres database](#add-a-postgres-database)[Provision the database](#provision-the-database)[Connect your Next.js service to Postgres](#connect-your-nextjs-service-to-postgres)[Run migrations with a pre-deploy command](#run-migrations-with-a-pre-deploy-command)[Next steps](#next-steps)[Edit this page on GitHub](https://github.com/railwayapp/docs/edit/main/content/guides/nextjs.md)Last updated Jun 21, 2026