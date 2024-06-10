import asyncio
import random

async def when_change():
    randomTime = random.randint(20, 20)
    await asyncio.sleep(randomTime)

async def choose_word(list):
    highest = 0
    output = []
    for word in list:
        if list[word]['count'] > highest:
            highest = list[word]['count']
    for word in list:
        if list[word]['count'] == highest:
            output.append(word)
    return output