import smtplib
import os
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIl_PASS')

msg = EmailMessage()
msg['Subject'] = 'Resume for digital harbour'
msg['from'] = EMAIL_ADDRESS
msg['to'] = 'kanojiya82@gmail.com'   #contacts
msg.set_content("Its sent from hotmail account")

files = [r'C:\Users\Ajay\Downloads\ajay.jpeg',r'C:\Users\Ajay\Downloads\Bandstand.jpeg',
         r'C:\Users\Ajay\Desktop\res_digital_harbour.pdf',r'C:\Users\Ajay\Desktop\for.py',
         r'C:\Users\Ajay\Downloads\salary.xlsx']
for file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='Application',subtype='Image',filename=file_name)


with smtplib.SMTP('smtp.live.com', 587) as smtp:
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)

