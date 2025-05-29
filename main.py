import smtplib
import json
import time
from web_request import * 






# Append to the end of your recipient phone number if sending email to sms
carrier = {
  "tmobile": "@tmomail.net", 
  "at&t":"@txt.att.net",
  "verizon": "@vtext.com",
  "sprint": "@messaging.sprintpcs.com"}


def sendmail(data: json):
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()

  s.login(data["email"], data["password"])
  message = "testing testing\n\n testing testing"

  s.sendmail(data["email"], f'{data["number"] + carrier["tmobile"]}', message)

  s.quit()


def timer(minutes): {
  # Since sleep counts in seconds we * 60
  time.sleep(minutes* 60)
}

def main() :
  with open("info.json", "r") as file:
    data = json.load(file)
  





if __name__ == 'main': 
  main()