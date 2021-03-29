# SMS AutoResponder API

A simple application that automatically responds to SMS messages using the Telnyx API

For the sake of simplicity, this application only responds to the following messages

- message containing `pizza` - `Chicago pizza is the best`
- message containing `ice cream` - `I prefer gelato`
- message not containing either of the above - `Please send either the word 'pizza' or 'ice cream' for a different response`

### TLDR

- Clone this git `git clone https://github.com/kcemenike/telnyx_autoresponder.git`
- Create virtual environment (optional)
- `cd telnyx_autoresponder`
- `pip install -r requirements.txt`
- Purchase a number in [Mission Control Portal](https://portal.telnyx.com/#/app/numbers/buy-numbers). Get credits
- Get [API key](https://portal.telnyx.com/#/app/api-keys)
- Create .env file using .env.sample as template
- Run `python src\app.py`

## Full Guide

Clone this git by running  
`git clone https://github.com/kcemenike/telnyx_autoresponder.git`

### Installing dependencies

#### Python >=3.5

Follow instructions to install the latest version of Python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

It is advised that you run this application in a virtual environment  
You can use conda or virtual-env to create a virtual environment

#### PIP dependencies

Once you have your virtual environment up and running, install dependencies by running:

```
pip install -r requirements.txt
```

This will install all the required packages specified in the `requirements.txt` file

#### Key dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.
- [Telnyx](https://telnyx.com) is a Cloud Platform As a Service (CPAAS) Provider

### Running the server (Windows/Linux)

To run the server, navigate to the project directory and run:  
`python src/app.py`

#### Optional (Linux in debug mode)

To run the server in Debug mode:

```
export FLASK_APP=api.py
export FLASK_ENV=debug
flask run --reload
```

#### Important

To communicate with the Telnyx Endpoint, you would need your service to be available over the internet. To do this, please use a tunneling service like ngrok. A simple guide is [here](https://developers.telnyx.com/docs/v2/development/ngrok)

### Environment variables

- **TELNYX_API_KEY**: Your Telnyx API V2 key. Get it from your [Mission Control Portal](https://portal.telnyx.com/) account and navigate to the Auth V2 tab in the "Auth" section.
- **PORT**: specifies the port you intend to run the server

## Testing

Run the tests by executing:

```
python src\test.py
```
