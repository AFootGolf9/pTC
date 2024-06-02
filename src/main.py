import asyncio
import TwitchValidation
from twitchAPI.chat import Chat, ChatMessage, EventData
from twitchAPI.type import ChatEvent

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
            words_dict[word] = {
                'word': word,
                'count': 1
            }
        else:
            words_dict[word]['count'] += 1

async def main():
    twitch = await TwitchValidation.get_twitch()
    chat = await TwitchValidation.get_chat(twitch)

    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)

    chat.start()

    try:
        input('Press enter to stop\n')
    finally:
        chat.stop()
        await twitch.close()
        for word in words_dict:
            print(f'{word}: {words_dict[word]["count"]} times')

if __name__ == '__main__':
    asyncio.run(main())