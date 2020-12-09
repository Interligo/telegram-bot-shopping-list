# Telegram bot to make and keep a shopping list 

![Python 3.7](https://img.shields.io/badge/python-v3.7-blue) ![Aiogram 2.9.2](https://img.shields.io/badge/aiogram-v2.9.2-yellow)

### What is this:

Personal bot-assistant which is deployed on Heroku, using free database https://restdb.io/, and is written with the framework aiogram.

The bot's main function is saving your shopping list at the database and making easier to plan shopping for your family.


### Who can use it:

Anyone who has half an hour to configure their own bot as instructed below.


### Getting started:

#### 1. Telegram bot token:

In Telegram find __@BotFather__ and send `/start` to it. Then send `/newbot` and give your bot the name. BotFather will send your a Telegram bot token. Save it and don't show it to anyone.


#### 2. Restdb.io:
[![rest-db-logo](https://ph-files.imgix.net/359437d3-7282-4aca-9410-8d8b6729c6fb?auto=format&auto=compress&codec=mozjpeg&cs=strip&w=339.8345498783455&h=221&fit=max)](https://restdb.io/)

So, here we are, click on the banner above to register. It is free and simple to use. After the registration you should create the first database - follow these instructions [quick start](https://restdb.io/docs/quick-start).

Did you make it? Great! Now we should connect to the database. There are many functions which work with the database, don't think about 'how it works': just let my code work for you.

To connect to your database open [database settings](https://github.com/Interligo/telegram-bot-shopping-list/blob/main/sl_db_settings.py) and put url into two strings: 
`URL = "YOUR DATABASE URL?q={}&sort=Category&dir=1"` - to get sorted shopping list and `SEARCH_URL = "YOUR DATABASE URL"`.

__All additional information you can get in [restdb docs](https://restdb.io/docs/)__.


#### 3. Heroku:
[![heroku-logo](https://camo.githubusercontent.com/6979881d5a96b7b18a057083bb8aeb87ba35fc279452e29034c1e1c49ade0636/68747470733a2f2f7777772e6865726f6b7563646e2e636f6d2f6465706c6f792f627574746f6e2e737667)](https://signup.heroku.com/)

If you are reading this, you have beaten the Restdb. At least, I hope so. Now we should make your app in heroku. Please press the button above.

You need to download [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).

Now we should write some code! Execute the following commands in your local command shell or terminal:

1. `heroku login` and log in to the Heroku CLI;
1. `git clone https://github.com/Interligo/telegram-bot-shopping-list.git`;
1. `cd telegram-bot-shopping-list`;
1. `heroku create -b heroku/python --region eu telegram-bot-shopping-list`;
1. `heroku git:remote telegram-bot-shopping-list`.

After that you should open [Heroku apps](https://dashboard.heroku.com/apps). Find __Settings__, __Config Vars__, press __Reveal Config Vars__ and paste your TELEGRAM_TOKEN which you've got in the first paragraph. Also you should add Telegram IDs of people who will use it into Config Vars. You may name them how you want.

Now go to the [handler](https://github.com/Interligo/telegram-bot-shopping-list/blob/main/handlers/sl_bot_handlers_other.py) and change `valid_ids = os.getenv('YOUR_NAME_OF_TELEGRAM_ID')` to let the bot know who will have the access to the database and to its fuctions.

And let's deploy the bot on Heroku - `git push heroku main`.

You can check the bot status `heroku ps` and read the logs 'heroku logs'.

__All additional information you can get in [heroku docs](https://devcenter.heroku.com/)__.

> P.S. Thank you for your time! I am glad that you've read all this text. I should warn you: this readme is written in English (haha, you, definetely, see it), but my bot will talk with you in Russian. People are strange creatures and I can't explain why I do this. Maybe to train my English? Ohhh...  
