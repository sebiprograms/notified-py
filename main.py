import json
from notified import *




def main():
  "Project Example webpage status updates via email to sms"
  with open("info.json", "r") as file:
    data = json.load(file)
  
  API_KEY = data["API_KEY"]
  url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"
  api(url, API_KEY)
  
  print("input type of time: min or sec\n")
  typeoftime = input()

  print("input quantity of time chosen\n")
  minsec = float(input())

  timer(typeoftime, minsec)
  msg = message(data, "This is a Notified App Alert\r\n", "Notified is an easy to use smtp python library allowing email to sms alerts")
  sendmail(data, msg)



main()

if __name__ == 'main': 
  main()