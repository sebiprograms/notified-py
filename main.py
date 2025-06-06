import smtplib
import json
import time
from notified import *
from web_request import * 



def main():
  "Project Example webpage status updates via email to sms"
  if (get_status('https://sebiprograms.github.io/admin-dashboard/') == 200):
    message = "Alert: Webpage is OK\n\n this is an notification from notify-py"
    print("page ok")
  else:
    message = "Alert: check webpage status\n\n this is an notification from notify-py"
    print("error check page")
  with open("info.json", "r") as file:
    data = json.load(file)
  
  print("input type of time: min or sec\n")
  typeoftime = input()

  print("input quantity of time chosen\n")
  minsec = float(input())

  timer(typeoftime, minsec)

  sendmail(data, message)



main()

if __name__ == 'main': 
  main()