---
title: Quick Start Tutorial
source: railway
url: https://docs.railway.com/quick-start
fetched: 2026-06-21T06:40:07.574579
---

# Quick Start Tutorial

* [Home](/)
* svg]:size-3.5">
* Quick start

# Quick Start Tutorial

On this pageRailway is a deployment platform that lets you provision infrastructure, develop locally with that infrastructure, and deploy to the cloud or simply run ready-made software from the template marketplace.


**This guide covers two different topics to get you quickly started with the platform -**


*
**Deploying your project** - Bring your code and let Railway handle the rest.


**[Option 1](/quick-start#deploying-your-project---from-github)** - Deploying from **GitHub**.


**[Option 2](/quick-start#deploying-your-project---with-the-cli)** - Deploying with the **[CLI](/cli)**.


**[Option 3](/quick-start#deploying-your-project---from-a-docker-image)** - Deploying from a **Docker Image**.


*
**Deploying a [template](reference/templates)** - Ideal for deploying pre-configured software with minimal effort.


To demonstrate deploying directly from a GitHub repository through Railway's dashboard, this guide uses a basic [NextJS app](https://github.com/railwayapp-templates/nextjs-basic) that was prepared for this guide.


For the template deployment, this guide uses the [Umami template](https://railway.com/deploy/umami) from the [template marketplace](https://railway.com/templates).


## [Deploying your project - from GitHub](#deploying-your-project---from-github)


If this is your first time deploying code on Railway, it is recommended to [forking](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the previously mentioned [NextJS app](https://github.com/railwayapp-templates/nextjs-basic)'s repository so that you can follow along.


To get started deploying your NextJS app, first make a new [project](/overview/the-basics#project--project-canvas).


*
Open up the [dashboard](/overview/the-basics#dashboard--projects) → Click **New Project**.


*
Choose the **GitHub repo** option.


![](https://res.cloudinary.com/railway/image/upload/v1723752559/docs/quick-start/new_project_uyqqpx.png)
*Railway requires a valid GitHub account to be linked. If your Railway account isn't associated with one, you will be prompted to link it.*


* Search for your GitHub project and click on it.


![](https://res.cloudinary.com/railway/image/upload/v1723752559/docs/quick-start/new_github_project_pzvabz.png)


*
Choose either **Deploy Now** or **Add variables**.


**Deploy Now** will immediately start to build and deploy your selected repo.


**Add Variables** will bring you to your service and ask you to add variables, when done you will need to click the **Deploy** button at the top of your canvas to initiate the first deployment.


*For brevity, choose **Deploy Now**.*


![](https://res.cloudinary.com/railway/image/upload/v1723752558/docs/quick-start/deploy_now_pmrqow.png)
When you click **Deploy Now**, Railway will create a new project for you and kick off an initial deploy after the project is created.


**Once the project is created you will land on your [Project Canvas](/quick-start#the-canvas)**.


## [Deploying your project - with the CLI](#deploying-your-project---with-the-cli)


As with the [Deploy from GitHub guide](/quick-start#deploying-your-project---from-github), if you're deploying code with the CLI for the first time, it's recommended to [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the [NextJS app](https://github.com/railwayapp-templates/nextjs-basic)'s repository to follow along. Since you'll be deploying local code, you'll also need to [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the forked repository.


The CLI can create a new project entirely from the command line, use it to scaffold your project.


*
Open up a command prompt inside your local project.


*
Run `railway init`


This will create a new empty project with the name provided, which will be used for any subsequent commands.


![](https://res.cloudinary.com/railway/image/upload/v1723752558/docs/quick-start/railway_init_rglt5w.png)
Deploying your code is now only a single command away.


*
Run `railway up`


The CLI will now scan your project files, compress them, and upload them to Railway's backend for deployment.


![](https://res.cloudinary.com/railway/image/upload/v1723752558/docs/quick-start/railway_up_vns3u4.png)
**You can now run `railway open` and you will taken to your [Project Canvas](/quick-start#the-canvas)**.


## [Deploying your project - from a Docker image](#deploying-your-project---from-a-docker-image)


Railway supports deploying pre-built Docker images from the following registries:


*
[Docker Hub](https://hub.docker.com)


*
[GitHub Container Registry](https://ghcr.io)


*
[RedHat Container Registry](https://quay.io)


*
[GitLab Container Registry](https://docs.gitlab.com/ee/user/packages/container_registry)


To get started deploying a Docker image, first make a new [project](/overview/the-basics#project--project-canvas).


*
Open up the [dashboard](/overview/the-basics#dashboard--projects) → Click **New Project**.


*
Choose the **Empty project** option.


![](https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1727281981/docs/quick-start/emptyproject_q8vqfz.png)
After the project is created, you will land on the [Project Canvas](/quick-start#the-canvas). A panel will appear prompting you to Add a Service.


![](https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1727281215/docs/quick-start/add_a_service.png)


* Click **Add a Service** and select the **Docker Image** option from the modal that pops up.


![](https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1727280789/docs/quick-start/select_docker_image_bdyltc.png)


* In the **Image name** field, enter the name of the Docker image, e.g, `blueriver/nextjs` and press Enter.


![](https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1727280788/docs/quick-start/blueriver_docker_image_zcn9py.png)
If you're using a registry other than Docker Hub (such as GitHub, GitLab, Quay), you need to provide the full Docker image URL from the respective registry.


![](https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1727280788/docs/quick-start/enter_docker_image_name_rzjbis.png)


* Press Enter and click **Deploy**.


Railway will now provision a new service for your project based on the specified Docker image.


And that's it! 🎉 Your project is now ready for use.


p]:my-1 [&>p:first-child]:mt-0 [&>p:last-child]:mb-0 [&_a]:underline [&_a]:underline-offset-2 [&_a:hover]:opacity-80">Private Docker registry deployments require the [Pro plan](/services#deploying-a-private-docker-image).


## [The canvas](#the-canvas)


Whether you deploy your project through the dashboard with GitHub or locally using the CLI, you'll ultimately arrive at your project canvas.


![](https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1723752560/docs/quick-start/project_canvas_nextjs_c6bjbq.png)
This is your *mission control*. Your project's infrastructure, [environments](/guides/environments), and [deployments](/guides/deployments) are all
controlled from here.


Once the initial deployment is complete, your app is ready to go. If applicable, generate a domain by clicking [Generate Domain](/guides/public-networking#railway-provided-domain) within the [service settings](/overview/the-basics#service-settings) panel.


**Additional Information -**


If anything fails during this time, you can explore your [build or deploy logs](/guides/logs#build--deploy-panel) for clues. A helpful tip is to scroll through the entire log; important details are often missed, and the actual error is rarely at the bottom!


If you're stuck don't hesitate to open a [Help Thread](https://station.railway.com/questions).


## [Deploying a template](#deploying-a-template)


Railway's [template marketplace](https://railway.com/templates) offers over 650+ unique templates that have been created both by the community and Railway!


Deploying a template is not too dissimilar to deploying a GitHub repo -


*
Open up the [dashboard](/overview/the-basics#dashboard--projects) → Click **New Project**.


*
Choose **Deploy a template**.


![](https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1723752559/docs/quick-start/template_new_project_k9kfrh.png)


*
Search for your desired template.


*Hint: If your desired template isn't found feel free to [reach out to the community](https://station.railway.com/questions).*


*
Click on the template you want to deploy.


![](https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1723752558/docs/quick-start/template_new_umami_j4la5d.png)
*Hint: Generally it's best to choose the template with a combined higher deployment and success count.*


*
Fill out any needed information that the template may require.


In the case of the Umami template, you don't need to provide any extra information.


![](https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1723752558/docs/quick-start/template_config_options_zaxbko.png)


* Click **Deploy**.


Railway will now provision a new project with all services and configurations that were defined in the template.


That's it, deploying a template is as easy as a few clicks!


![](https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1723752560/docs/quick-start/project_canvas_umami_lb759i.png)
## [Closing](#closing)


Railway aims to be the simplest way to develop, deploy, and diagnose issues with your application.


As your Project scales, Railway scales with you by supporting multiple Teams, vertical scaling, and horizontal scaling; leaving you to focus on what matters: your code.


Happy Building!


### [What to explore next](#what-to-explore-next)


*
**[Environments](/environments)** - Railway lets you create parallel, identical environments for PRs/testing.


*
**[Observability Dashboard](/observability)** - Railway's built-in observability dashboard offers a customizable view of metrics, logs, and usage in one place.


*
**[Project Members](/projects/project-members)** - Adding members to your projects is as easy as sending them an invite link.


*
**[Staged Changes](/deployments/staged-changes)** - When you make changes to your Railway project, such as adding or removing components and configurations, these updates will be gathered into a changeset for you to review and apply.


### [Join the community](#join-the-community)


Chat with Railway members, ask questions, and hang out in the [Railway Discord community](https://discord.gg/railway) with fellow builders! We'd love to have you!

[NextThe basics](/overview/the-basics)### On this page

[Deploying your project - from GitHub](#deploying-your-project---from-github)[Deploying your project - with the CLI](#deploying-your-project---with-the-cli)[Deploying your project - from a Docker image](#deploying-your-project---from-a-docker-image)[The canvas](#the-canvas)[Deploying a template](#deploying-a-template)[Closing](#closing)[What to explore next](#what-to-explore-next)[Join the community](#join-the-community)### Ask AI about this page

Copy pageOpen in ChatGPTOpen in ClaudeOpen in Cursor[Edit this page on GitHub](https://github.com/railwayapp/docs/edit/main/content/docs/quick-start.md)Last updated Jun 20, 2026