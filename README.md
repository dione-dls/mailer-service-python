# Mail Service

Mail Service is a nameko service that sends a plaintext email using the Mailgun API whenever an event is received from Payment Service.

Payment Service is a nameko service that dispatches an event every 10 seconds. Each dispatched event carries a payload which contains
client, payee, and transaction information. These details are then used by the Mail Service to complete and format a boilerplate email
which notifies the payee that payment has been made to him/her by a client.

## Getting Started

Using your command line, clone the repository to your local machine

```sh
git@github.com:dione-dls/mailer-service-python.git

```
Switch to the cloned repo and install:
* Nameko

```sh
pip install nameko
```

* Pytest
```sh
pip install pytest
```
* Faker
```sh
pip install fake-factory
```
Install RabbitMQ using Homebrew:

```sh
brew install rabbitmq
```

And set up an account with Mailgun to get the services running. You may sign up for a free account here:

https://www.mailgun.com/ .

You will then need to update the information in the config.py file (API key, email, and domain) using your own Mailgun account information.
All of these can be found on your main Mailgun dashboard.

## Aproach to Solving the Problem

## Running the Program

Open three separate terminals.

Run RabbitMQ in the first:

Run MailService in the second:

Run PaymentService in the third:

## Areas for Improvement
