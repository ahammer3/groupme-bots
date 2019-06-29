This was a quick groupme bot that I implemented using the following 2 resources:

1) https://github.com/BenDMyers/Boilerplate_GroupMe_Bot
2) http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/

MAIN FUNCTION: The main function of this bot is an adaptation of the popular r/freefolk "Bobby B" bot on reddit. I was a big fan of this bot and during the huge hype of GoT season 8, I decided this would be a fun little thing to implement for my groups on groupme, to personalize Bobby B a little bit. Basically, whenever his name is called, he will simply shout out a popular phrase that his character had in the show. It's all just pointless fun.

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

5) bobbyb.txt
    I gathered all of Robert Baratheon's famous quotes here. My favorite ones are duplicated. They can be added to, deleted from, or manipulated very easily.

To get started, one should create a test environment (empty group) in groupme and head over to their bot dev domain, where they can learn the ropes pretty quickly:
1)  https://dev.groupme.com/bots

Happy botting!
