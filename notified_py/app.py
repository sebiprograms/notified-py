import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.kwargs_injection.args import *
import json

def no_bot_messages(message, next):
    subtype = message.get("subtype")
    if subtype != "bot_message":
        next()



with open('info.json', 'r') as file:
    data = json.load(file)


app = App(token=data['bot_user_auth'],)



handler = SocketModeHandler(app, data['xapp'])

@app.event(event="app_mention")
def test_mention():
    print("bot was mentioned in Slack")


handler.start()



