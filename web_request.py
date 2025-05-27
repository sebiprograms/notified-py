import requests

#Return status code 
def get_status(): 
  r = requests.get('https://sebiprograms.github.io/admin-dashboard/')
  return r.status_code


