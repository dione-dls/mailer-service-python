import requests


class MailService(object):
    name = 'mail'
    
    def on_payment_received(self, param):
        return {
            'client': {
                'name': 'John Doe',
                'email': 'john.doe@mailexample.com'
            },
            'payee': {
                'name': 'Jane Doe',
                'email': 'jane.doe@mailexample.com'
            },
            'payment': {
                'amount': 9000,
                'currency': 'USD'
            }
        }