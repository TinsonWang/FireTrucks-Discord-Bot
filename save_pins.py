import discord
import os
import requests
import shutil
import time
from misc import standardize_struct_time, standardize_datetime


async def save_pins(message, client):

    print('\n!savepins command used by {} on {}.\n'.format(message.author, time.asctime(time.localtime())) +
          'Starting save_pins function...')

    await message.channel.send('Alright, let me look for those pins...')

    if len(message.content) < 10:
        channel_id = client.channels.general_chat.id
    else:
        channel_id = int(message.content[10:])

    try:
        channel_name = client.get_channel(channel_id).name
    except:
        await message.channel.send('Unable to get the specified channel. Check your channel ID input.')
        print('Unable to get the specified channel. Check your channel ID input.')
        print('save_pins function closing...')
        return

    text_pins = []

    folder_name = standardize_struct_time(time.localtime()) + ' ' + message.guild.name \
                  + ' ' + client.get_channel(channel_id).name

    save_dir = os.path.join(os.getcwd(), folder_name)
    os.makedirs(save_dir)
    print('New folder made: {}'.format(save_dir))

    print('Grabbing pins from {}...'.format(client.get_channel(channel_id).name))
    pins = await client.get_channel(channel_id).pins()
    print('Finished grabbing pins.')

    pin_counter = 1

    for pin in pins:

        print('Saving {}/{} pins...'.format(pin_counter, len(pins)))
        pin_counter += 1

        if not pin.attachments:
            text_pins.append(pin)
        else:
            for attachment in pin.attachments:

                i = 0

                file_type = attachment.filename[-4:]

                if file_type == '.exe':
                    continue

                valid_author_filename = "".join(x for x in pin.author.name if (x.isalnum() or x in "._- "))
                new_filename = '[' + standardize_datetime(pin.created_at) + '] ' + valid_author_filename + ' '

                if not pin.content:
                    new_filename += str(i)
                    i += 1
                else:
                    new_filename += "".join(x for x in pin.clean_content if (x.isalnum() or x in "._- "))

                new_filename += file_type

                save_file_dir = os.path.join(save_dir, new_filename)

                r = requests.get(attachment.url)
                with open(save_file_dir, 'wb') as file:
                    file.write(r.content)

    text_filename = 'text_pins.txt'

    with open(os.path.join(save_dir, text_filename), 'w') as file:
        for text_message in text_pins:
            file.write('[' + str(text_message.id) + ']\n[' + str(text_message.created_at)
                       + '] ' + text_message.author.name + ':\n' + text_message.content + '\n\n\n')


    print('Creating .zip file...')
    shutil.make_archive(save_dir, 'zip', save_dir)

    file = discord.File(save_dir + '.zip', filename=save_dir + '.zip')

    destination_channel = client.channels.chalkboard.id

    print('Sending .zip file...')
    await client.get_channel(destination_channel).send(
        content='New pins package from {}!'.format(client.get_channel(channel_id).name), file=file)

    await message.channel.send('All done packaging and sending the pins!')

    print('Deleting save directory...')
    shutil.rmtree(save_dir)
    print('Save directory deleted. save_pins function is now done.\n')