import smtplib
import json
import time
from web_request import * 


activate = False

with open("info.json", "r") as file:
  data = json.load(file)

# Append to the end of your recipient phone number if sending email to sms
carrier = {
  "tmobile": "@tmomail.net", 
  "at&t":"@txt.att.net",
  "verizon": "@vtext.com",
  "sprint": "messaging.sprintpcs.com"}


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
  
s.login(data["email"], data["password"])
message = "Testing Testing"

print("type in minutes when you'd like a notification to be sent")
timer = input() * 60
clock = time.time()



s.sendmail(data["email"], f'{data["number"] + carrier["tmobile"]}', message)
s.quit()



