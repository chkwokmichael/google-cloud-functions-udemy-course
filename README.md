# Google Cloud Functions Course
## -- Google Cloud Functions (FaaS) with Python from zero to hero!

This is an Udenmy course on Google Cloud Functions. This repo is to hold all the course materials.

## Starting a project
To start a new project in Google Cloudm we can go to the [Firebase Console](https://console.firebase.google.com) or create it from [Google Cloud Platform Console](https://console.cloud.google.com).

## Creating a virtual environment
** Please note that the follow codes are for MacOS specifically.

First, install `python3`.
```
brew install virtualenv
```

Then, enter the following command tp create the virtual environment.
```
python3 -m venv venv
```

To activate the virtual environment, run the following command.
```
source venv/bin/activate
```

In order to add new packages to our new virtual env, we create a file alled `requirements.txt`  and run the following command.
```
pip install -r requirements.txt
```
## Deploying our functions
First, we have to set our project ID with the folowing command:
```
gcloud config set project [PROJECT_ID]
```

Then, we deploy our function with the following command:
```
gcloud functions deploy [FUNCTION_NAME] --runtime python[VERSION] --trigger-http
```

Here's an example:
```
gcloud functions deploy hello_world --runtime python39 --trigger-http
```

## Deploying our cloud functions with environment variables and other dependencies
First, create a `.env.yml` file and a `requirements.txt` in the same directory of the `main.py` file.
Then, runt ht following command in the terminal to deploy it to GCP
```
gcloud functions deploy [FUNCTION_NAME] --env-vars-file [ENV_VAR_FILE_NAME] --runtime python[VERSION] --trigger-http
```

Here's an example:
```
gcloud functions deploy send_mail --env-vars-file .env.yml --runtime python39 --trigger-http
```

### Scheduling our cloud functions
First, we need to install the required package.
```
gcloud components install beta
gcloud components update
```
Then, we create a pubsub topic and subscribe to it.
```
gcloud pubsub topics create [TOPIC_NAME]
gcloud pubsub subscriptions create cron-sub --topic [TOPIC_NAME]
```

### Deleting cloud functions
Run the following commands,
```
gcloud functions delete [FUNCTION_NAME]
```