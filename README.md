# SMS AutoResponder (Telnyx)

A simple application that automatically responds to SMS messages using the Telnyx API

## How it works

- Sign up on Telnyx and [get a Telnyx number](https://portal.telnyx.com/#/app/numbers/buy-numbers)
- Deploy this application
- Send an SNS to your Telnyx number and you should get a custom auto-response

For the sake of simplicity, this application only responds to messages using the following logic:

- message containing **`pizza`** will be responded with `Chicago pizza is the best`
- message containing **`ice cream`** will be responded with `I prefer gelato`
- message not containing either of the above will be responded with `Please send either the word 'pizza' or 'ice cream' for a different response`

You can edit this mapping by modifying the MAPPING object in [constants.py](src/constants.py)  
You can also set the default value by modifying the DEFAULT object in [constants.py](src/constants.py)

<img src="assets/img/img.jpg" alt="image" width="50%"/>

## Quick setup

- Clone this git `git clone https://github.com/kcemenike/telnyx_autoresponder.git`
- Create virtual environment (optional)
- `cd telnyx_autoresponder`
- `pip install -r requirements.txt`
- Purchase a number in [Mission Control Portal](https://portal.telnyx.com/#/app/numbers/buy-numbers).
- Get [API key](https://portal.telnyx.com/#/app/api-keys)
- Create .env file using .env.sample as template
- Run `python src\app.py`
- Create a messaging profile in [Mission Control Panel](https://portal.telnyx.com/#/app/messaging), assign it to the number you purchased, and add a webhook to it. The webhook is https://{YOUR_PUBLIC_ADDRESS}/webhooks or an address you configure if you're using a [tunneling tool like ngrok](https://developers.telnyx.com/docs/v2/development/ngrok) or [webhook.site](https://webhook.site)
- Send a message to your purchased number and see the auto-responder in action :-)

## Full Guide

Clone this git by running  
`git clone https://github.com/kcemenike/telnyx_autoresponder.git`

### Installing dependencies

#### Python >=3.5

Follow instructions to install the latest version of Python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

It is advised that you run this application in a virtual environment  
You can use [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) or [venv](https://docs.python.org/3/library/venv.html) to create a virtual environment

#### PIP dependencies

Once you have your virtual environment up and running, install dependencies by running:

```
pip install -r requirements.txt
```

This will install all the required packages specified in the `requirements.txt` file

#### Key dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend micro-service framework. Flask is required to handle requests and responses.
- [Telnyx](https://telnyx.com) is a next-generation Cloud Platform As a Service (CPaaS) Provider that provides carrier-grade services on a global, private IP network.

### Running the server (Windows/Linux)

To run the server, navigate to the project directory and run:  
`python src/app.py`

#### Optional (Linux in debug mode)

To run the server in Debug mode:

```
export FLASK_APP=src/app.py
export FLASK_ENV=debug
flask run --reload
```

#### Important

To communicate with the Telnyx Endpoint, you would need your service to be available over the internet. To do this, please use a tunneling service like ngrok. A simple guide is [here](https://developers.telnyx.com/docs/v2/development/ngrok)

### Environment variables

A sample `.env.sample` can be used as a template. The environment variables are below:

- **TELNYX_API_KEY**: Your Telnyx API V2 key. Get it from your [Mission Control Portal](https://portal.telnyx.com/) account and navigate to the Auth V2 tab in the "Auth" section.
- **PORT**: specifies the port you intend to run the server

## Testing

Run the tests by executing:

```
python src\test.py
```
