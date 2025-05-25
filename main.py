import json
def main():
  with open('info.json', 'r') as openfile:
    data = json.load(openfile)
  
  print(data)
  










if __name__ =="__main__":
  main()