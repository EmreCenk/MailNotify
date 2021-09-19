from email.mime import image
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import*

import os
from dotenv import load_dotenv
load_dotenv()
exampleUsername = os.environ["USERNAME123123123"]
examplePassword = os.environ["PASSWORD123123123"]

class email:

  @staticmethod
  def send(email,img):
    
    tod = date.today() #date
    today=str(tod)
    now = datetime.now()
    gettime = str(now.strftime("%H:%M:%S"))
    
    # print("USERNAME:",exampleUsername)
    # print("PASSWORD", examplePassword)

    # Define these once; use them twice!
    strFrom = "OfficialMailBoxNotifier"
    strTo = email

    
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Mailbox alert'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'Mailbox has just been triggered at '+today+'! Here are the details:'


    msgAlternative = MIMEMultipart('')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText(today + " at "+gettime)
    msgAlternative.attach(msgText)

   
    msgText = MIMEText('<br><b>The Mailbox Notifier has been triggered!</b><br>Here is the image of the delievery inside the mailbox: <br><img src="cid:image1" style="width:700px;height:500px" alt="Inside mailbox"><br><script>const b = new Date(); document.getElementById("date").innerHTML = b;</script>', 'html')
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory

    file = open(img, "rb")
    msgImage = MIMEImage(file.read())
    file.close()
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    # Send the email (this example assumes SMTP authentication is required)
    import smtplib
    smtp = smtplib.SMTP("smtp.gmail.com:587")
                                                      #contacts the server
    smtp.connect("smtp.gmail.com:587")

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()


    smtp.login(exampleUsername, examplePassword)

    smtp.sendmail(strFrom, strTo, msgRoot.as_string())  #logins

    smtp.quit()
    print('sent successfully')

if __name__ == "__main__":
    email.send("ridwan3968@gmail.com","server_/test_image.png") #Sends test email