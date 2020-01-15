import time

async def clear_pins(message, client):

    print('\n!clearpins command used by {} on {}.\n'.format(message.author, time.asctime(time.localtime())) +
          'Starting clear_pins function...')

    await message.channel.send('Alright, let me clear those pins...')

    if len(message.content) < 11:
        channel_id = client.channels.general_chat.id
    else:
        channel_id = int(message.content[11:])

    try:
        channel_name = client.get_channel(channel_id).name

    except:
        await message.channel.send('Unable to get the specified channel. Check your channel ID input.')
        print('Unable to get the specified channel. Check your channel ID input.')
        print('clear_pins function closing...')
        return

    print("Grabbing pins from {}...".format(client.get_channel(channel_id).name))
    pins = await client.get_channel(channel_id).pins()
    print("Finished grabbing pins.")

    pin_counter = 1

    for pinned_message in pins:
        print("Clearing {}/{} pins...".format(pin_counter, len(pins)))
        pin_counter += 1
        await pinned_message.unpin()


    await message.channel.send("All pins have been cleared from the {} channel, sir!".format(channel_name))