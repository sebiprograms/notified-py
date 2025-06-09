import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.kwargs_injection.args import *
import json

with open('info.json', 'r') as file:
    data = json.load(file)

# Initilization
app = App(token=data['bot_user_auth'],)


# Allows socket connection so web requests don't 
# need to be handled manually
handler = SocketModeHandler(app, data['xapp'])

# Any eventlisteners or middleware goes here
@app.event(event="app_mention")
def test_mention():
    print("bot was mentioned in Slack")


handler.start()



