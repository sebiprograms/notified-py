import smtplib

carrier = {
  "tmobile": "@tmomail.net", 
  "at&t":"@txt.att.net",
  "verizon": "@vtext.com",
  "sprint": "messaging.sprintpcs.com"}

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
  
s.login("user", "pass")
message = "Subject\n\n Message"
  
s.sendmail("sender", "reciever", message)
s.quit()



