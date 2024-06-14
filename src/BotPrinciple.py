import asyncio
import random

async def when_change():
    randomTime = random.randint(60, 90)
    await asyncio.sleep(randomTime)

async def choose_word(list):
    highest = 0
    output = []
    for word in list:
        if list[word] > highest:
            highest = list[word]
    for word in list:
        if list[word] == highest:
            output.append(word)
    return output

async def sort_words(list):
    highest = 0
    sorted_list = {}
    for word in list:
        if list[word] > highest:
            highest = list[word]
    for i in range(highest, 0, -1):
        for word in list:
            if list[word] == i:
                sorted_list[word] = i
    return sorted_list