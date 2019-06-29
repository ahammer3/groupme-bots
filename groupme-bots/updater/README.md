This was a quick groupme bot that I implemented using the following 2 resources:

1) https://github.com/BenDMyers/Boilerplate_GroupMe_Bot
2) http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/

MAIN FUNCTION: The main function of this bot is an "updater". If you are away from groupme for a few hours in the day, you can simply have the updater fill you in quickly on the most popular messages that were written while you were gone so you dont have to keep scrolling up. This is tedious especially if your group is very large.

Resources that helped - through my own research:

1) https://groupy.readthedocs.io/en/master/_modules/groupy/api/messages.html
2) https://dashboard.heroku.com/
3) https://groupy.readthedocs.io/en/latest/pages/quickstart.html#messages

FILES:

1) app.py
    This contains the main code to run the bot. Comments are included, and it should be pretty self explanatory. 
    
2) Procfile
    Needed for heroku app to run correctly.
    
3) requirements.txt
    Needed for heroku app to run correctly.
    
4)  runtime.txt
    Needed for heroku app to run correctly.
    
    To get started, one should create a test environment (empty group) in groupme and head over to their bot dev domain, where they can learn the ropes pretty quickly:
   1)  https://dev.groupme.com/bots
   
Happy botting!
