from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import json
with open('info.json', 'r') as file:
    data = json.load(file)


app = App(token=data['bot_user_auth'],)


