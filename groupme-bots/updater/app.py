# IMPORTS
import os
import json
import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request
from groupy import Client

# Start the app
app = Flask(__name__)
bot_id = "YOUR BOT ID HERE"

# connect to groupme
token = 'YOUR TOKEN HERE'
client = Client.from_token(token)
groups = list(client.groups.list_all())

# make sure the group you're trying to get exists
group = None
for x in groups:
    if x.name == 'YOUR GROUP NAME HERE':
        group = x

# adapted from https://github.com/BenDMyers/Boilerplate_GroupMe_Bot
# Called whenever the app's callback URL receives a POST request
# That'll happen every time a message is sent in the group
@app.route('/', methods=['POST'])
def webhook():
    # 'data' is an object that represents a single GroupMe message.
    data = request.get_json()

    # get the daily leaderboard with groupy
    best_day = group.leaderboard.list_day()
    
    # update counter
    no_update = 0

    # We don't want to reply to ourselves!
    # to update with all leaderboard messages - any message in the day that has more than 3 likes
    if "update-me-all" in data['text'].lower() and not sender_is_bot(data):
        for obj in best_day:
            if len(obj.favorited_by) >= 3:
                msg = obj.name + " said: " + obj.text + " - likes: " + str(len(obj.favorited_by))
                reply(msg)

    # to update since the user last spoke - same concept
    elif "update-me" in data['text'].lower() and not sender_is_bot(data):

        # get the last time the user spoke (not including just now)
        messages = group.messages.list_all()
        generate_since = None
        first_pass = False

        for message in messages:
            if message.name == data['name']:
                if first_pass:
                    generate_since = message.created_at
                    break
                first_pass = True

        for obj in best_day:
            if obj.created_at > generate_since:
                if len(obj.favorited_by) >= 3:
                    no_update += 1

        # no need to update if it was uneventful
        if no_update < 2:
            reply("Nope.")

        else:
            for obj in best_day:
                if obj.created_at > generate_since:
                    if len(obj.favorited_by) >= 3:
                        msg = obj.name + " said: " + obj.text + " - likes: " + str(len(obj.favorited_by))
                        reply(msg)

    # I added this for a fun example - says something every time a specific person says something
    elif data['text'].lower() == "SOMETHING FUN HERE" and data['name'] == "SPECIFIC GROUP MEMBER":
        reply("BOT RESPONSE HERE")

    return "ok", 200

################################################################################
# code below is from https://github.com/BenDMyers/Boilerplate_GroupMe_Bot - only reply was really used
################################################################################

# Send a message in the groupchat
def reply(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id'        : bot_id,
        'text'            : msg
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

# Send a message with an image attached in the groupchat
def reply_with_image(msg, imgURL):
    url = 'https://api.groupme.com/v3/bots/post'
    urlOnGroupMeService = upload_image_to_groupme(imgURL)
    data = {
        'bot_id'        : bot_id,
        'text'            : msg,
        'picture_url'        : urlOnGroupMeService
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

# Uploads image to GroupMe's services and returns the new URL
def upload_image_to_groupme(imgURL):
    imgRequest = requests.get(imgURL, stream=True)
    filename = 'temp.png'
    postImage = None
    if imgRequest.status_code == 200:
        # Save Image
        with open(filename, 'wb') as image:
            for chunk in imgRequest:
                image.write(chunk)
        # Send Image
        headers = {'content-type': 'application/json'}
        url = 'https://image.groupme.com/pictures'
        files = {'file': open(filename, 'rb')}
        payload = {'access_token': 'eo7JS8SGD49rKodcvUHPyFRnSWH1IVeZyOqUMrxU'}
        r = requests.post(url, files=files, params=payload)
        imageurl = r.json()['payload']['url']
        os.remove(filename)
        return imageurl

# Checks whether the message sender is a bot
def sender_is_bot(message):
    return message['sender_type'] == "bot"
