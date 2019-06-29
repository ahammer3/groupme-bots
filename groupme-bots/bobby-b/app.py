# IMPORTS
import os
import json
import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

# connect to groupme
app = Flask(__name__)
bot_id = "YOUR BOT ID HERE"

# open and read the quotes
with open("bobbyb.txt") as f:
    lines = [line.rstrip('\n') for line in f]

# adapted from https://github.com/BenDMyers/Boilerplate_GroupMe_Bot
# Called whenever the app's callback URL receives a POST request
# That'll happen every time a message is sent in the group
@app.route('/', methods=['POST'])
def webhook():
    # 'data' is an object that represents a single GroupMe message.
    data = request.get_json()

    # very simple bot...
    if "bobby b" in data['text'].lower():
        # I realized that random.randint has been said to not truly be random, but it was close enough for the purposes of this bot
        i = random.randint(0,50)
        
        msg = lines[i]
        reply(msg)

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
