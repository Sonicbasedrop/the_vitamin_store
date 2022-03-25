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
9. Add Heroku app name to ALLOWED_HOSTS in settings.py.
10. Commit changes to GitHub using git add ., git commit -m and the commit message, then git push.
11. Then deploy to Heroku using git push heroku main
If the git remote isn't initialised you may have to do that first by running heroku git:remote -a "heroku-app-name"
12. Create a superuser using command: heroku run python3 manage.py createsuperuser so that you can log in to admin as required.
13. From Heroku dashboard click "Deploy" -> "Deployment Method" and select "GitHub"
14. Search for your GitHub repo and connect then Enable Automatic Deploys.
15. Generate secret key. Strong secret keys can be obtained from [RandomKeygen](https://randomkeygen.com/). This automatically generates a secret key 50 characters long with alphanumeric characters and symbols. 
16. Add secret key to GitPod variables and Heroku config vars.
17. Set up Amazon AWS S3 bucket using instructions [below](#amazon-aws)
18. In the dashboard click "Settings" -> "Reveal Config Vars"
19. Set [config vars](#config-vars) using advice below.

#### Amazon AWS

1. Create Amazon AWS account and create a new bucket in the S3 services and choose your closest region.
2. Uncheck block all public access and create bucket. 
3. From Properties tab turn on static website hosting using default values of index.html and errors.html.
4. On permissions tab include CORS configuration:
```python
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
5. Create security policy: S3 Bucket Policy, allow all principles by adding a "*" and Amazon S3 services and selecting Get Object action. Paste ARN from Bucket Policy, add statement, generate policy and copy and paste into Bucket Policy. Also add "/*" at end of resource key to allow use of all pages. 
6. Under public access select access to all List Objects. 

7. Create Group for the bucket through IAM. Create policy by importing AWS S3 Full Access policy and add ARN from bucket to the policy resources. Attach policy to group. 
8. Create user, give programmatic access and add user to the group. Download CSV file when prompted to save access key ID an secret access key to save to environment and config [variables](#config-vars).
9. Add AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME = 'eu-north-1' to settings.py.
10. Add, commit and push to GitHub then navigate to Heroku to confirm static files collected successfully on the Build Log. The DISABLE_COLLECTSTATIC variable can now be deleted. 

#### gmail Client

In 'settings.py' change the 'DEFAULT_FROM_EMAIL' to your own email address.

1. Go to your Gmail account and navigate to the 'Settings' tab.
2. Go to 'Accounts and Imports', 'Other Google Account Settings'.
3. Go to the 'Security' tab, and scroll down to 'Signing in to Google'.
4. If required, click to turn on '2-step Verification', then 'Get Started', and enter your password.
5. Verify using your preferred method, and turn on 2-step verification.
6. Go back to 'Security', 'Signing in to Google', then go to 'App Passwords'.
7. Enter your password again if prompted, then set 'App' to 'Mail', 'Device' to 'Other', and type in 'Django'.
8. Copy and paste the passcode that shows up, this is your 'EMAIL_HOST_PASS' variable to add to your environment/config variables. 'EMAIL_HOST_USER' is the Gmail email address.


