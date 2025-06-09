import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.kwargs_injection.args import *
import json

with open('info.json', 'r') as file:
    data = json.load(file)

class Notified_slack:
    """
    Creates a slack bot, event handling can be created
    by
    @name_of_object.app.event()
        def func():
            event handling here 
    Uses sockets not http request
    """
    with open('info.json', 'r') as file:
        data = json.load(file)
    def __init__(self):
        self.app = App(token=data['bot_user_auth'])
    def start(self):
        handler = SocketModeHandler(self.app, data['xapp'])
        handler.start()
        # Allows socket connection so web requests don't 
        # need to be handled manually

# Creates 
bot = Notified_slack()

# Any eventlisteners or middleware goes here
@bot.app.event(event="app_mention")
def test_mention():
    print("bot was mentioned in Slack")

bot.start()


