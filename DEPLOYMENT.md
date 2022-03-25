Back to my main README.md click [here](https://github.com/Sonicbasedrop/the_vitamin_store/blob/main/README.md#the-vitamin-store)
<br>

## Deployment Steps

### Table of Content

* [Heroku Deployment](#heroku-deployment)
* [Connecting to Heroku](#connecting-to-heroku)
* [Amazon AWS](#amazon-aws)
* [gmail Client](#gmail-client)
* [Config Vars](#config-vars)
* [How to contribute to the site](#how-to-contribute-to-the-site)
* [How to run the project locally](#how-to-run-the-project-locally)


### Heroku Deployment

#### Connecting to Heroku

The project was developed using [GitPod](https://gitpod.io/) and pushed to [GitHub](https://github.com/) then deployed on Heroku using these instructions:

1. Log in to Heroku and create a new app by clicking "New" and "Create New App" and giving it an original name and setting the region to closest to your location.
2. Navigate to Heroku Resources and add Postgres using the free plan.
3. Create a requirements.txt file using command pip3 freeze > requirements.txt
4. Create a Procfile with the terminal command web: gunicorn the_vitamin_store.wsgi:application* and at this point checking the Procfile to make sure there is no extra blank line as this can cause issues when deploying to Heroku.
5. Use the loaddata command to load the fixtures for both json files: python3 manage.py loaddata categories.json* and python3 manage.py loaddata products.json
6. If it returns error message: django.db.utils.OperationalError: FATAL: role "somerandomletters" does not exist* run unset PGHOSTADDR in your terminal and run the commands in step 11 again.
7. From the CLI log in to Heroku using command heroku login -i.
8. Temporarily disable Collectstatic by running: heroku:config:set DISABLE_COLLECTSTATIC=1 --app "heroku-app-name" So that Heroku won't try to collect static files when we deploy.

