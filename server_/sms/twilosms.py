# from dotenv import load_dotenv
# load_dotenv()
import os
from twilio.rest import Client
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
send = Client(account_sid, auth_token)
class sms:
    def send(phonenumber,image_url):
        send.messages.create(from_=os.environ.get('TWILIO_PHONE_NUMBER'),
                      to=phonenumber,
                      media_url=[image_url],
                      body='Mailbox has been opened. Check your mailbox for new items now!')
        print("sent sms successfully")


if __name__ == '__main__':
    sms.send('+12265074010',"https://i.insider.com/61135525ad63f30019501966?width=700")