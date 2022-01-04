### Начинаем работу:

#### 1. Токен для Telegram бота:

В Telegram следует найти __@BotFather__ и отправить ему `/start`. Затем отправьте `/newbot`, придумайте отображаемое имя и имя пользователя для бота. Затем BotFather отправит токен бота. Сохраните его в безопасном месте. Кроме того, тут же можно задать перечень команд бота и сменить его аватар.


#### 2. База данных Restdb.io:
[![rest-db-logo](https://ph-files.imgix.net/359437d3-7282-4aca-9410-8d8b6729c6fb?auto=format&auto=compress&codec=mozjpeg&cs=strip&w=339.8345498783455&h=221&fit=max)](https://restdb.io/)

Для регистрации аккаунта в Restdb.io нажмите на баннер выше. Это абсолютно бесплатно и просто в использовании. После регистрации следует создать первую облачную базу данных - следуйте данной инструкции [quick start](https://restdb.io/docs/quick-start).

Получилось? Замечательно! Теперь следует подключиться к базе данных. Я описал несколько фукнций для взаимодействия с базой данных, не думайте о том, 'как именно это работает': просто позвольте моему коду работать на вас.

Для подключения к базе данных откройте [database settings](https://github.com/Interligo/telegram-bot-shopping-list/blob/main/sl_db_settings.py) и измените две строки: 
`URL = "YOUR DATABASE URL?q={}&sort=Category&dir=1"` - для получения отсортированного списка покупок и `SEARCH_URL = "YOUR DATABASE URL"`.

__Вся дополнительная информация здесь - [restdb docs](https://restdb.io/docs/)__.


#### 3. Площадка для бота Heroku:
[![heroku-logo](https://camo.githubusercontent.com/6979881d5a96b7b18a057083bb8aeb87ba35fc279452e29034c1e1c49ade0636/68747470733a2f2f7777772e6865726f6b7563646e2e636f6d2f6465706c6f792f627574746f6e2e737667)](https://signup.heroku.com/)

Если вы дошли до этой части инструкции, то вы одолели Restdb. Как минимум, я надеюсь на это. Теперь нам следует создать свое приложение heroku. Нажмите на кнопку выше.

Установите приложение [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).

Теперь напишем немного кода! Выполните следующие команды в своем терминале:

1. `heroku login` и авторизуйтесь в Heroku CLI;
1. `git clone https://github.com/Interligo/telegram-bot-shopping-list.git`;
1. `cd telegram-bot-shopping-list`;
1. `heroku create -b heroku/python --region eu telegram-bot-shopping-list`;
1. `heroku git:remote telegram-bot-shopping-list`.

После этого откройте [Heroku apps](https://dashboard.heroku.com/apps). Найдите __Settings__, __Config Vars__, нажмите __Reveal Config Vars__ и вставьте свой TELEGRAM_TOKEN, который мы получили в первом абзаце. Кроме того, добавьте Telegram IDs, которые должны иметь доступ к боту в 'Config Vars'. Вы можете назвать их как угодно.

Теперь откройте [handler](https://github.com/Interligo/telegram-bot-shopping-list/blob/main/handlers/sl_bot_handlers_other.py) и измените `valid_ids = os.getenv('YOUR_NAME_OF_TELEGRAM_ID')` для того чтобы бот знал, кто должен иметь доступ к базе данных и его функциях.

Теперь давайте задеплоим бота на Heroku - `git push heroku main`.

Вы можете проверить статус бота с помощью команды `heroku ps`, а ознакомиться с логами с помощью - `heroku logs`.

__Вся дополнительная информация здесь - [heroku docs](https://devcenter.heroku.com/)__.

