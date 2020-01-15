import discord


class RoleList:

    def __init__(self, client):

        self.tinson = client.get_guild(452322376345190431).get_role(452332026385661967)

        self.wency = client.get_guild(452322376345190431).get_role(452332556369526784)

        self.veterans = client.get_guild(452322376345190431).get_role(574111353770344448)

        self.upper_role = client.get_guild(452322376345190431).get_role(574116140129845249)

        self.middle_role = client.get_guild(452322376345190431).get_role(574118259742212117)

        self.starter_role = client.get_guild(452322376345190431).get_role(574118262632349706)
