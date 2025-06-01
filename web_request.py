import requests

#Return status code 
def get_status(website: str): 
  r = requests.get(website)
  return r.status_code


