from channel_list import ChannelList
from role_list import RoleList
from tow_alerts import *
from googletrans import Translator
from save_pins import save_pins
from stats import *
from text_adventure import *
from translate_message import *
from plot import *
from logger import *
from clear_pins import *

idle = discord.Game("with it's own existence")


# Modified discord.Client() class
class ft_Client(discord.Client):

    def __init__(self, prefix, *args, **kwargs, ):
        super().__init__(*args, **kwargs)
        self.prefix = prefix

    async def on_ready(self):

        self.activity_tracker = {}
        self.messages = 0
        self.joined = 0
        self.x_value = []
        self.y_value = []

        self.channels = ChannelList(self)
        self.roles = RoleList(self)
        self.translator = Translator()

        print('Logged in as ' + str(self.user))
        print('------')

        self.loop.create_task(update_stats(self))

        await self.channels.bot_channel.send("I am ready to take orders, sir!")
        await self.change_presence(status=discord.Status.online, activity=idle)

    async def on_message(self, message):

        self.messages += 1
        message_cache[message.id] = message.content

        alerts = discord.Game("ToW Event Alerts: On")

        # Makes sure the bot doesn't respond to its own message in case it contains keywords.
        if message.author == self.user:
            return

        if str(message.author) in self.activity_tracker:
            self.activity_tracker[str(message.author)] += 1
        if str(message.author) not in self.activity_tracker:
            self.activity_tracker[str(message.author)] = 1

        if message.content.lower().find("idiot") != -1:
            if message.author.top_role.permissions.administrator:
                await message.channel.send("Yeah, I agree...")
            else:
                await message.channel.send("No, you're the idiot!")

        # Scans the first char of the message string to make sure it has the correct
        # command prefix. Otherwise, the message is NOT a command and the rest of the if statements
        # below are ignored.
        #
        # It SHOULD improve performance... -Wency
        try:
            if message.content[0] != self.prefix:
                return

        except IndexError:
            pass

        # Administrator only commands go in this branch.
        if message.author.top_role.permissions.administrator:

            if message.content[1:9] == 'savepins':
                await save_pins(message, self)
                return

            if message.content[1:10] == 'clearpins':
                await clear_pins(message, self)
                return

            if message.content[1:10] == 'towalerts':
                await self.channels.bot_channel.send("You have turned on alerts for Tales of Wind!")
                self.tow_alerts_task = self.loop.create_task(tow_alerts(self))
                await self.change_presence(status=discord.Status.online, activity=alerts)
                return

            if message.content[1:10] == "alertsoff":
                self.tow_alerts_task.cancel()
                await self.channels.bot_channel.send("You have turned off alerts for Tales of Wind!")
                await self.change_presence(status=discord.Status.online, activity=idle)
                return

            if message.content.lower()[1:6] == "stats":
                with open("stats.txt") as sts:
                    final_stats = sts.readlines()
                await message.channel.send(final_stats[-1])
            if message.content.lower()[1:6] == "clear":
                await clear_stats(self)
                await message.channel.send("The stats log has been cleared, sir!")
            if message.content.lower()[1:5] == "wipe":
                await clear_logs(self)
                await message.channel.send("The messages log has been wiped, sir!")

            if message.content.lower()[1:9] == "activity":
                await message.channel.send(self.activity_tracker)

            if message.content.lower()[1:5] == "plot":
                await graph(message, self)

        if message.content.lower()[1:3] == "to":
            # See translate_message.py
            await translate_message(self, message)

        if message.content.lower()[1:15] == "text_adventure":
            await message.channel.send(
                "Starting up adventure game as Player " + str(message.author) + ". We hope you enjoy your experience!")
            await text_adventure(message)

    async def on_member_join(self, member):
        self.joined += 1
        await self.channels.general_chat.send(
            "Hey! A new friend arrived at the door! Everyone please welcome " + member.mention + " !")
        autorole = discord.utils.get(member.guild.roles, id=574118262632349706)
        await member.add_roles(autorole)

    async def on_member_remove(self, member):
        await self.channels.admin_chat.send("Farewell young " + member.display_name + " ...")

    async def on_disconnect(self):
        await self.channels.bot_channel.send("I'm signing off now!")

    async def on_message_delete(self, message):
        await logger(message)
