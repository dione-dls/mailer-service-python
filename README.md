# Mail Service

Mail Service is a nameko service that sends a plaintext email using the Mailgun API whenever an event is received from Payment Service.

Payment Service is a nameko service that dispatches an event every 10 seconds. Each dispatched event carries a payload which contains
client, payee, and transaction information. These details are then used by the Mail Service to complete and format a boilerplate email. This email, once delivered serves as notification to the payee that payment has been made to him/her by a client.

## Getting Started

Using your command line, clone the repository to your local machine:

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
All of these can be found on your Mailgun dashboard.

## Running the Program

Before running the program, make sure you have switched to python 3.

You may run the app in the command line by opening three separate command line terminals.

Run RabbitMQ in the first:
```sh
rabbitmq-server
```

Run MailService in the second:
```sh
nameko run MailService
```

Run PaymentService in the third:
```sh
nameko run PaymentService
```
When all services are started, MailService will send out payment confirmation emails for each event dispatched by PaymentService.

A sample email delivered by MailService via Mailgun is as follows:
```sh
Dear Christopher Nguyen,

You have received a payment of 6323 USD from Andrea Nelson (mahoneymorgan@example.com).

Yours,

Student.com
```
## Running the Test

The following command will run both the unit and integration test for MailService:
```sh
pytest
```

## Areas for Improvement
Given more time to be familiar with python, pytest, and nameko, I would write more robust unit and integration tests to ensure all the parts of the program are working as expected. Also, given more time, it would have been nice to include, among others, code which will guard againsts incorrect/missing information being dispatched by PaymentService as well as error messages to check whether MailService has been successful in delivering the email (e.g. a Response 200 if mail was delivered).

