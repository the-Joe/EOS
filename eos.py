import os
import re
import eos_access
from flask import Flask, request
from slack_sdk import WebClient, WebhookClient
from slack_bolt import App, Say
from slack_bolt.adapter.flask import SlackRequestHandler
app = Flask(__name__)
client = WebClient(token=eos_access.SLACK_BOT_TOKEN)
bolt_app = App(token=eos_access.SLACK_BOT_TOKEN, signing_secret=eos_access.SLACK_SIGNING_SECRET)


@bolt_app.message("hello sauron")
def greetings(payload: dict, say: Say):
    """ This will check all the message and pass only those which has 'hello sauron' in it """
    user = payload.get("user")
    say(f"Hi <@{user}>")

@bolt_app.message(re.compile("(hi|hello|hey) sauron"))
def reply_in_thread(payload: dict):
    """ This will reply in thread instead of creating a new thread """
    response = client.chat_postMessage(channel=payload.get('channel'),
                                     thread_ts=payload.get('ts'),
                                     text=f"Hi <@{payload['user']}>")
@bolt_app.command("/sauron")
def help_command(say, ack):
    ack()
    text = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "This is a slash command"
                }
            }
        ]
    }
    say(text=text)


handler = SlackRequestHandler(bolt_app)


@app.route("/sauron/events", methods=["POST"])
def slack_events():
    """ Declaring the route where slack will post a request """
    return handler.handle(request)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=True)

