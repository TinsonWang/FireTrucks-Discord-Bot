import discord
from discord.ext import commands

async def connect(context):

    try:
        # voice.channel = VoiceChannel class in the API
        vc = context.author.voice.channel
        channel = vc.name

        if channel != None:
            print('Connecting to: ' + channel)
            await vc.connect()

    except AttributeError:
        await context.message.channel.send("You must be connected to a voice channel first!")

async def disconnect(context):

    try:
        #voice_client = VoiceClient class in the API
        await context.voice_client.disconnect(force=True)

    except AttributeError:
        await context.message.channel.send("You must be connected to a voice channel first!")