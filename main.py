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



on = False

print("type in minutes when you'd like a notification to be sent (greater than 0)")

start = float(input()) * 60

if start > 0:
  on = True
else:
  print("type in minutes when you'd like a notification to be sent (greater than 0)")
  start = input() * 60

while on:
  currenttime = time.time()

  if currenttime >= start:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
  
    s.login(data["email"], data["password"])
    message = "Testing Testing"

    s.sendmail(data["email"], f'{data["number"] + carrier["tmobile"]}', message)

    s.quit()
    exit



