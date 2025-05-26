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
  
s.login(data["email"], data["password"])
message = "Testing Testing"
  
s.sendmail(data["email"], f'{data["number"] + carrier["tmobile"]}', message)
s.quit()



