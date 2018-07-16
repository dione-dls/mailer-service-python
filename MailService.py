import requests

class MailService(object):
    name = 'mail'
    subject = 'Payment Received'
    body = """\
    Dear {payee},
    You have received a payment of {amount} {currency} from {client} ({email}).
    Yours,
    student.com
    """
    
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