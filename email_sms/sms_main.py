from twilio.rest import Client
from email_sms import config
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


def send_sms():
    client = Client(config.ACCOUNT_SID, config.AUTH_TOKEN)
    message = client.messages.create(
        to=config.MY_NUMBER,
        from_=config.FROM_NUMBER,
        body='Testing'
    )
    print(message)


app = Flask(__name__)


@app.route('/')
def homepage():
    return 'All working!'


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    from_number = request.form['From']
    body = request.form['Body']
    resp = MessagingResponse()
    msg = (f'Awwwww! Thanks so much for your message {from_number}, '
           f'"{body}" to you too. ')
    resp.message(msg)
    return str(resp)


if __name__ == '__main__':
    app.run()