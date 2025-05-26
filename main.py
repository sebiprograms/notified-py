import smtplib
import json

with open("info.json", "r") as file:
  data = json.load(file)


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



