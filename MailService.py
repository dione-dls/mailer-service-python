import requests
import config

from nameko.events import event_handler, BROADCAST

class MailService(object):
    name = 'mail'
            
    @event_handler('payments', 'payment_received', handler_type=BROADCAST, reliable_delivery=False)
    def on_payment_received(self, payload):
        success = False
        try:
            self.send_mail(payload)
            success = True
        except Exception as e:
            print(e.message)
        finally:
            return success
    
    def send_mail(self, payload):
        print("payment received:", payload)
        return requests.post(
            config.domain,
            auth=("api", config.api_key),
            data = self.format_text(payload))
            
    def format_text(self, payload):
        return {
                "from": config.mail_from,
                "to": config.mail_to,
                "subject": "Payment received",
                "text": ("""
                    Dear {},
                    You have received a payment of {} {} from {} ({}).
                    Yours,
                    Student.com
                    """).format(
                    (payload['payee']['name']),(payload['payment']['amount']),
                    (payload['payment']['currency']), (payload['client']['name']),
                    (payload['client']['email']))}