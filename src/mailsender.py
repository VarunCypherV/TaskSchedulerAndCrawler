##SEND MAIL WITH ATTACHMENTS AS WELL 
import os
import smtplib
from email.message import EmailMessage
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


def sendEmail(imgpath,receiverEmail):
    if EMAIL_ADDRESS is None or EMAIL_PASSWORD is None:
        print("Please set the EMAIL_ADDRESS and EMAIL_PASSWORD environment variables.")
    else:
        msg = EmailMessage()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = receiverEmail
        msg['Subject'] = "Test Subject"
        msg.set_content("Test Body")

        ##ADD FOR ATTACHMENT REMOVE IF NOT REQUIRED
        with open(imgpath, "rb") as image_file:
            image_data = image_file.read()
            msg.add_attachment(image_data, maintype='image', subtype='jpeg', filename="cat.jpeg")

        # with open("cat.pdf", "rb") as pdf_file:  # Change "example.pdf" to the actual path of your PDF file
        #     pdf_data = pdf_file.read()
        #     msg.add_attachment(pdf_data, maintype='application', subtype='pdf', filename="cat.pdf")

        with smtplib.SMTP('smtp.outlook.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

