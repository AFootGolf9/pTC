# pTC - python Twitch Bot

## Introduction

basic bot, made with the goal to read all messages in a twitch chat and
show which word was most said, listing all words and how many times that word was said

## How it works

the project is separeted in 2 parts the bot and a flask app that periodically
recives data to show the results.

### The bot

The twitchAPI is used for access to twitch and is made that after each message recived by the bot it
will separate words by space between words and save that word case is a new one, in case it already exists
it will add to the count of the word. Periodically all the words will be sorted and sent to the flask app,
and the list will be emptied and the process continues.

### Flask app

When accessed will return all words and their counts in a html ordered list, also has a post endpoint
to receive new data

## Requirements

- Python
- Twitch credentials

## How to use

1. Clone Repository
2. Run setup.sh
3. add your credentials in Bot/res/config.ini
4. change variable chanel in Bot/src/main.py to the chanel you want it to hear
5. run start.sh it, will start both the bot and the flask app(it may ask for you to log in your twitch acount)
6. open your browser in localhost:5000