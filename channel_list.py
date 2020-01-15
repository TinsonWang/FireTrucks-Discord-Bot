class ChannelList:

    def __init__(self, client):

        self.general_chat = client.get_channel(452380439949082624)

        self.admin_chat = client.get_channel(452353992136065024)

        self.bot_channel = client.get_channel(575769518127841281)

        self.chalkboard = client.get_channel(452353042554028032)

        self.giant_monitor = client.get_channel(579932161109655558)
