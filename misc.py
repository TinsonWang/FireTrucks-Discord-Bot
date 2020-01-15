# Miscellaneous functions
import emoji
import asyncio
import time


def remove_emojis_from_string(string):

    new_string = string

    for character in new_string:
        if character in emoji.UNICODE_EMOJI:
            new_string = new_string.replace(character, '')

    return new_string


async def my_background_task(client):
    while not client.is_closed():
        await client.get_channel(575769518127841281).send('this is the background task')
        await asyncio.sleep(5)  # task runs every 60 seconds


def remove_tags(a):
    while a.find('<') != -1:

        a = a.strip()

        left = a.find('<')
        right = a.find('>')

        if left == 0:
            a = a[right + 1: len(a)]
        else:
            a = a[: left]

    return a.strip()


def standardize_struct_time(struct_time):
    if struct_time[1] < 10:
        month = '0' + str(struct_time[1])
    else:
        month = str(struct_time[1])

    if struct_time[2] < 10:
        day = '0' + str(struct_time[2])
    else:
        day = str(struct_time[2])

    date = str(struct_time[0]) + month + day

    return date


def standardize_datetime(datetime):
    if datetime.month < 10:
        month = '0' + str(datetime.month)
    else:
        month = str(datetime.month)

    if datetime.day < 10:
        day = '0' + str(datetime.day)
    else:
        day = str(datetime.day)

    date = str(datetime.year) + month + day

    return date

