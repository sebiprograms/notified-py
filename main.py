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


def timer(typeoftime: str, minsec: float):
  """
  sleeps typeoftime for unit's long

  typeoftime can be min or sec
  """
  if (((typeoftime != "min") & (typeoftime != "sec")) | (minsec <= 0)):
    print("invalid input, or no time added skipping timer")
    return
  elif (typeoftime == "min"):
    time.sleep(minsec * 60)
  elif (typeoftime == "sec"):
    time.sleep(minsec)


def main():
  with open("info.json", "r") as file:
    data = json.load(file)
  
  print("input type of time: min or sec\n")
  typeoftime = input()

  print("input quantity of time chosen\n")
  minsec = float(input())
  timer(typeoftime, minsec)
  sendmail(data)
  
 


main()

if __name__ == 'main': 
  main()