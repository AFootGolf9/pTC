import asyncio
import TwitchValidation
from BotPrinciple import when_change, sort_words
from twitchAPI.chat import ChatMessage, EventData
from twitchAPI.type import ChatEvent
import requests

words_said = []
words_dict = {}

async def on_ready(ready: EventData):
    print('Chat is ready')

    await ready.chat.join_room('afootgolf9')

async def on_message(msg: ChatMessage):
    msg_words = msg.text.split(' ')
    for word in msg_words:
        if word not in words_said:
            words_said.append(word)
            words_dict[word] = 1
        else:
            words_dict[word]+= 1

async def main():
    global words_dict
    global words_said
    theWord = ""
    twitch = await TwitchValidation.get_twitch()
    chat = await TwitchValidation.get_chat(twitch)

    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)

    chat.start()

    while True:
        await when_change()
        sorted_words = sort_words(words_dict)
        words_dict = {}
        words_said = []
        sorted_words = await sorted_words

        requests.post('http://localhost:5000/update', json=sorted_words)

if __name__ == '__main__':
    asyncio.run(main())