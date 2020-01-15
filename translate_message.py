from googletrans import LANGUAGES


async def translate_message(client, message):
    # Extracts the 'destination code' from the command
    dest = message.content.lower()[3:message.content.index(' ')]

    if dest == 'chs':
        dest = 'zh-cn'

    if dest == 'cht':
        dest = 'zh-tw'

    if dest == 'jp':
        dest = 'ja'

    if dest not in LANGUAGES:
        await message.channel.send('Invalid language code - try again? :thinking:')
        return
    else:
        message_translated = client.translator.translate(message.content[6:], dest=dest)
        await message.channel.send(str(message.author) + ' [' + message_translated.src + ' -> '
                                   + message_translated.dest + ']:\n' + message_translated.text)
        return