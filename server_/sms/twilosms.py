from dotenv import load_dotenv
load_dotenv()
import os
from twilio.rest import Client
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
send = Client(account_sid, auth_token)
class sms:

    @staticmethod
    def send(phonenumber):
        send.messages.create(from_=os.environ.get('TWILIO_PHONE_NUMBER'),
                      to=phonenumber,
                      body='Mailbox has been opened. Check your mailbox for new items now!')


if __name__ == '__main__':
    sms.send('+15197215818')