import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.image import MIMEImage

server_email = "panshu614@gmail.com"
server_passkey = "pojx xwpa sxax expa"
smtp_port = 587
smtp_server = "smtp.gmail.com"

#setting up email
sender_email = server_email
receiver_emails = ['pandeyan7878@gmail.com', 'hrideshp2@gmail.com', 'aashishmora@gmail.com', 'sameerbasnet10@gmail.com', 'thapabishal423@gmail.com']
subject = 'this is python generetd email'
body = 'hello this is something body'

email = MIMEMultipart()
email['From'] = sender_email
email['To'] =  ', '.join(receiver_emails)
email['Subject'] = subject


email.attach(MIMEText(body,'plain'))


file = "Desktop/camel.jpg"
with open(file ,'rb') as img_file:
   img = MIMEImage(img_file.read())

img.add_header('Content-Disposition', f'attachment ; filename = camelkophoto')
email.attach(img)
   

# send a email
 
try:
   
   with smtplib.SMTP(smtp_server,smtp_port) as server:
      server.starttls()
      server.login(server_email,server_passkey)
      text = email.as_string()
      server.sendmail(sender_email,receiver_emails,text)
      print(" EMAIL SENT SUCCESSFULLY ")

except Exception as e:
   print (f" DUE TO {e} REASON WE COULD NOT SEND MAIL")



