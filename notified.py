import json 
import smtplib

# Append to the end of your recipient phone number if sending email to sms
#Specifices the mobile carrier's 
#domain name. Must be appended to phone number
#in -> sendmail(sender, recievernumber@carrierdomain.com, message)
carrier = {
  "tmobile": "@tmomail.net", 
  "at&t":"@txt.att.net",
  "verizon": "@vtext.com",
  "sprint": "@messaging.sprintpcs.com"}


def sendmail(data: json, message: str):
  """
  Sends messages through mail via SMTP 
  using googles smtp server.

  Password must be an app password can be created
  in google settings. 
  """
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()

  s.login(data["email"], data["password"])

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