import smtplib
import json
import time
from notified import *



def main():
  "Project Example webpage status updates via email to sms"



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