import smtplib


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
  
s.login("user", "password")
message = "Subject\n\n Message"
  
s.sendmail("sender", "reciever", message)
s.quit()



