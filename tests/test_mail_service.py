from nameko.testing.services import worker_factory


import sys
sys.path.insert(0, '..')

from MailService import MailService
from PaymentService import PaymentService

class TestMailService(object):
    def get_payload(self):
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

    def test_mail_service_unit(self):
        mail_service = worker_factory(MailService)
        payload = self.get_payload()
        
        assert mail_service.on_payment_received(payload)

        # del payload['payee']
        # assert mail_service.on_payment_received(payload) == False