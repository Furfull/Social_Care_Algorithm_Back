from app.parameters import ACCOUTSID, AUTHTOKEN
from twilio.rest import Client

def send():
    client = Client(ACCOUTSID, AUTHTOKEN)

    client.messages \
                    .create(
                        body="""Olá, vamos celebrar a amizade. \n
                        Que tal perguntar como está o dia de Levi Gabriel?""",
                        from_='+12294146075',
                        to='+5521970272132'
                    )
    return "OK"