# EduTatar client as Telegram Bot
This bot allows to get watch timetables, marks, reminders and whole statistics about your study based on edu.tatar.ru

## Installation
Install all dependencies (from root directory):
```
pip install -e .
pip install -r requirements.txt
```
1. Setup a database (default is SQLite)
2. Configure the config file in this path: **edu_tatar_bot/config/config.ini** (delete .example.)

## Run
```
cd edu_tatar_bot
python main/bot.py
```
