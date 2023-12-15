from twilio.rest import Client
import config

class WhatsApp:
    def __init__(self):
        self.client = None

    def conectar(self):
        self.client = Client(config.ACCOUNT_SID, config.AUTH_TOKEN )
        return True

    def enviar_mensagem(self, mensagem):
        message = self.client.messages.create(
            from_=f'whatsapp:{config.PHONE_TWILIO}',
            body=f'{mensagem}',
            to=f'whatsapp:{config.DESTINATARIO}'
        )
       
