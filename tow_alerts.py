import discord
import time
import asyncio
import random


async def tow_alerts(client):
    # await self.wait_until_ready()
    kingdom = (11, 13, 15, 17, 19, 23)
    kingdommsg = ("There is a Kingdom Event going on right now! :crown: ",
                  "Earn Kingdom Points through the Kingdom Event happening right now! :crown: ",
                  "This just in: there's an active Kingdom Event! :crown: ")
    bug_hunt1 = range(11, 23, 1)
    bug_hunt2 = (15, 45)
    bughuntmsg = ("There are bugs everywhere! Get rid of them all during this Bug Hunt Event right now! :beetle: ",
                  "The Bug Hunt Event is taking place right now! Clean this place up, will you? :beetle: ",
                  "Snifflers have popped up everywhere! Do your part and exterminate them during this Bug Hunt Event! :beetle: ")
    treasure_hunt = (14, 22)
    treasuremsg = ("Beat them into the ground! Treasure Hunter Event is on! :moneybag: ",
                   "Did anyone say treasure? The Treasure Hunter Event is going on right now! :moneybag: ",
                   "A little PvP couldn't hurt, right? The Treasure Hunter Event is on! :moneybag: ")
    world_boss = (12, 16, 22)
    worldbossmsg = ("A bunch of bosses just spawned! Good luck with the World Boss! :map: ",
                    "Secure the loot! World Bosses have spawned! :map: ",
                    "Go go go, the World Bosses have just arrived! :map: ")
    zodiac1 = range(11, 24, 1)
    zodiacmsg = ("Do you believe in the Zodiac? Zodiac Bosses have spawned! :dizzy: ",
                 "What is your lucky color? The Zodiac Bosses have appeared! :dizzy: ",
                 "The Zodiac Bosses have just spawned! Fight them to earn equipment enhancement materials! :dizzy: ")
    snowfightmsg = ("Get your throwing arm ready! The Snow Fight is on! :snowflake: ",
                    "Take aim...ready...throw! Take part in the Snow Fight now! :snowflake: ",
                    "When did it get so chilly in here...? Give it your all in the Snow Fight! :snowflake: ")
    guildballmsg = (
        "Get your dancing shoes on because it's time to get your groove on at the Guild Ball! :man_dancing::dancer: ",
        "Grab a partner and swing your hips because it's time for the Guild Ball! :man_dancing::dancer: ",
        "I hope you remember how to dance because everyone's waiting for you at the Guild Ball! :man_dancing::dancer: ")
    apocalypsemsg = ("Apocalypse is open today! Let's get that bread :bread: ",
                     "The end of the world is here...just kidding! Apocalypse is open today! :pray: ",
                     "EXP and Cards? Count me in! Make sure you take part in Apocalypse today! :money_with_wings: ")
    raccoonsmsg = (
        "The Raccoons and their leader Old Wombat are stealing our funds again! Please head over to the Guild Territory! :chipmunk: ",
        "Thieves! Thieves! Kick them out of the Guild Territory now! :chipmunk: ",
        "The Raccoons brought their leader with them again? We'll show them a lesson! Head on over to the Guild Territory! :chipmunk: ")
    guildwarmsg = ("Everyone, to arms! It's Guild War time! Tonight we fight for FireTrucks!:fire_engine: ",
                   "Give your hearts! Fight for FireTrucks in this Guild War! :fire_engine: ",
                   "It's time to pull all the stops! Give it your all in the Guild War for FireTrucks! :fire_engine: ")
    racingmsg = ("Get your betting chips ready because it's time for Racing! :racehorse: ",
                 "Which jockey looks the best today? The bets have opened for Racing! :racehorse: ",
                 "Fancy your luck? Bring your chips and head on over to Laplace to place your bets for Racing! :racehorse: ")
    overlordmsg = ("The Overlord Event is on! Do your best! Give it your all! :crossed_swords: ",
                   "Do your best to dish out as much damage as possible! The Overlord Event is on! :crossed_swords: ",
                   "Let's all work together to earn FireTrucks a high score! Take part in the Overlord Event now! :crossed_swords: ")
    calamitymsg = ("Challenge the Calamity Bosses in the Calamity Strikes Event now! :star2:",
                   "Are you prepared for the Boss Rush? Try your hand at the Calamity Strikes Event! :star2: ",
                   "Form a team to take on the Calamity Strike Event happening right now! :star2: ")
    celestialmsg = ("How far can you go? The Celestial Tower is open right now! :japanese_castle:",
                    "Grab your friends and scale the Celestial Tower! It's open today! :japanese_castle: ",
                    "Sweet rewards await those who challenge the Celestial Tower! Give it a shot! :japanese_castle: ")
    wellstudied1msg = (
        "It's time to put on our thinking caps! The Well-Studied Event is open now! :pencil2::book: ",
        "You better touch up on those trivia skills because the Well-Studied Event is going on now! :pencil2::book: ",
        "Pssst, what's the answer to question 3? The Well-Studied Event is taking place right now! :pencil2::book: ")
    wellstudied2msg = (
        "How'd you do? The Well-Studied Event Finals are open now! You have 10 minutes until entrance closes. Good luck everyone! :pencil2::book: ",
        "The door is open for those who did well in the earlier Well-Studied Event! One more time, you can do it! :pencil2::book: ",
        "Did you get here by cheating? That's okay - I did too. The Well-Studied Finals are open now! :pencil2::book: ")
    miragemsg = ("The Mirage Event is happening right now! Catch those piggies! :pig: ",
                 "Will you roll high? Will you roll low? Test your luck at the Mirage Event! :pig: ",
                 "Take part in the Mirage Event now for a chance to earn a ton of rare items! :pig: ")
    ruins_boss = (15, 23)
    ruinsmsg = (
        "A powerful entity named the Ancient Ruin Boss has spawned! Take it down for awesome rewards! :moyai: ",
        "Take on the Ancient Ruin Bosses to earn gemstones used for Star Trail! :moyai: ",
        "The Ancient Ruins Bosses aren't so scary when we fight together! Challenge them as a team and earn rewards together! :moyai: ")
    giant_monitor = client.get_channel(579932161109655558)
    firetrucks = client.guilds[0]
    towrole = firetrucks.get_role(576630527868665856)
    while not client.is_closed():
        # Monday Events
        if time.localtime()[6] == 0:
            for i in kingdom:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(kingdommsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            for i in world_boss:
                if time.localtime()[3] == i and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                    await giant_monitor.send(worldbossmsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            for i in treasure_hunt:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(treasuremsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            if time.localtime()[3] == 21 and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                await giant_monitor.send(snowfightmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 20 and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                await giant_monitor.send(guildballmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 6 and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                await giant_monitor.send(apocalypsemsg[random.randint(0, 2)])
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 19 and time.localtime()[4] == 50 and time.localtime()[5] == 0:
                await giant_monitor.send(raccoonsmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            for i in bug_hunt1:
                for j in bug_hunt2:
                    if time.localtime()[3] == i and time.localtime()[4] == j and time.localtime()[5] == 0:
                        await giant_monitor.send(bughuntmsg[random.randint(0, 2)])
                        await asyncio.sleep(1)
                    else:
                        pass

            await asyncio.sleep(1)
        else:
            pass

        # Tuesday Events
        if time.localtime()[6] == 1:
            for i in kingdom:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(kingdommsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            for i in world_boss:
                if time.localtime()[3] == i and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                    await giant_monitor.send(worldbossmsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            for i in treasure_hunt:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(treasuremsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            if time.localtime()[3] == 21 and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                await giant_monitor.send(guildwarmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 19 and time.localtime()[4] == 50 and time.localtime()[5] == 0:
                await giant_monitor.send(raccoonsmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            for i in bug_hunt1:
                for j in bug_hunt2:
                    if time.localtime()[3] == i and time.localtime()[4] == j and time.localtime()[5] == 0:
                        await giant_monitor.send(bughuntmsg[random.randint(0, 2)])
                        await asyncio.sleep(1)
                    else:
                        pass

            for i in zodiac1:
                if time.localtime()[3] == i and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                    await giant_monitor.send(zodiacmsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            await asyncio.sleep(1)
        else:
            pass

        # Wednesday Events
        if time.localtime()[6] == 2:
            for i in kingdom:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(kingdommsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            for i in world_boss:
                if time.localtime()[3] == i and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                    await giant_monitor.send(worldbossmsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            for i in treasure_hunt:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(treasuremsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            if time.localtime()[3] == 6 and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                await giant_monitor.send(apocalypsemsg[random.randint(0, 2)])
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 20 and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                await giant_monitor.send(guildballmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 21 and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                await giant_monitor.send(racingmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 19 and time.localtime()[4] == 50 and time.localtime()[5] == 0:
                await giant_monitor.send(raccoonsmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            for i in bug_hunt1:
                for j in bug_hunt2:
                    if time.localtime()[3] == i and time.localtime()[4] == j and time.localtime()[5] == 0:
                        await giant_monitor.send(bughuntmsg[random.randint(0, 2)])
                        await asyncio.sleep(1)
                    else:
                        pass

            await asyncio.sleep(1)
        else:
            pass

        # Thursday Events
        if time.localtime()[6] == 3:
            for i in kingdom:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(kingdommsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            for i in world_boss:
                if time.localtime()[3] == i and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                    await giant_monitor.send(worldbossmsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            for i in treasure_hunt:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(treasuremsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            if time.localtime()[3] == 21 and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                await giant_monitor.send(guildwarmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 19 and time.localtime()[4] == 50 and time.localtime()[5] == 0:
                await giant_monitor.send(raccoonsmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            for i in zodiac1:
                if time.localtime()[3] == i and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                    await giant_monitor.send(zodiacmsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            for i in bug_hunt1:
                for j in bug_hunt2:
                    if time.localtime()[3] == i and time.localtime()[4] == j and time.localtime()[5] == 0:
                        await giant_monitor.send(bughuntmsg[random.randint(0, 2)])
                        await asyncio.sleep(1)
                    else:
                        pass

            await asyncio.sleep(1)
        else:
            pass

        # Friday Events
        if time.localtime()[6] == 4:
            for i in kingdom:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(kingdommsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            for i in world_boss:
                if time.localtime()[3] == i and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                    await giant_monitor.send(worldbossmsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            for i in treasure_hunt:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(treasuremsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            if time.localtime()[3] == 20 and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                await giant_monitor.send(guildballmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 6 and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                await giant_monitor.send(apocalypsemsg[random.randint(0, 2)])
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 21 and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                await giant_monitor.send(overlordmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 19 and time.localtime()[4] == 50 and time.localtime()[5] == 0:
                await giant_monitor.send(raccoonsmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            for i in bug_hunt1:
                for j in bug_hunt2:
                    if time.localtime()[3] == i and time.localtime()[4] == j and time.localtime()[5] == 0:
                        await giant_monitor.send(bughuntmsg[random.randint(0, 2)])
                        await asyncio.sleep(1)
                    else:
                        pass

            for i in ruins_boss:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(ruinsmsg[random.randint(0, 2)] + towrole.mention)
                    await asyncio.sleep(1)
                else:
                    pass

            await asyncio.sleep(1)
        else:
            pass

        # Saturday Events
        if time.localtime()[6] == 5:
            for i in kingdom:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(kingdommsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            for i in world_boss:
                if time.localtime()[3] == i and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                    await giant_monitor.send(worldbossmsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            for i in treasure_hunt:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(treasuremsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            if time.localtime()[3] == 21 and time.localtime()[4] == 10 and time.localtime()[5] == 0:
                await giant_monitor.send(calamitymsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 13 and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                await giant_monitor.send(celestialmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 19 and time.localtime()[4] == 50 and time.localtime()[5] == 0:
                await giant_monitor.send(raccoonsmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            for i in bug_hunt1:
                for j in bug_hunt2:
                    if time.localtime()[3] == i and time.localtime()[4] == j and time.localtime()[5] == 0:
                        await giant_monitor.send(bughuntmsg[random.randint(0, 2)])
                        await asyncio.sleep(1)
                    else:
                        pass

            for i in ruins_boss:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(ruinsmsg[random.randint(0, 2)] + towrole.mention)
                    await asyncio.sleep(1)
                else:
                    pass

            for i in zodiac1:
                if time.localtime()[3] == i and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                    await giant_monitor.send(zodiacmsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            await asyncio.sleep(1)
        else:
            pass

        # Sunday Events
        if time.localtime()[6] == 6:
            for i in kingdom:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(kingdommsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            if time.localtime()[3] == 6 and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                await giant_monitor.send(apocalypsemsg[random.randint(0, 2)])
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 13 and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                await giant_monitor.send(wellstudied1msg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 20 and time.localtime()[4] == 50 and time.localtime()[5] == 0:
                await giant_monitor.send(wellstudied2msg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            if time.localtime()[3] == 20 and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                await giant_monitor.send(guildballmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            for i in treasure_hunt:
                if time.localtime()[3] == i and time.localtime()[4] == 0 and time.localtime()[5] == 0:
                    await giant_monitor.send(treasuremsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            if time.localtime()[3] == 21 and time.localtime()[4] == 20 and time.localtime()[5] == 0:
                await giant_monitor.send(miragemsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            for i in world_boss:
                if time.localtime()[3] == i and time.localtime()[4] == 30 and time.localtime()[5] == 0:
                    await giant_monitor.send(worldbossmsg[random.randint(0, 2)])
                    await asyncio.sleep(1)
                else:
                    pass

            if time.localtime()[3] == 19 and time.localtime()[4] == 50 and time.localtime()[5] == 0:
                await giant_monitor.send(raccoonsmsg[random.randint(0, 2)] + towrole.mention)
                await asyncio.sleep(1)
            else:
                pass

            for i in bug_hunt1:
                for j in bug_hunt2:
                    if time.localtime()[3] == i and time.localtime()[4] == j and time.localtime()[5] == 0:
                        await giant_monitor.send(bughuntmsg[random.randint(0, 2)])
                        await asyncio.sleep(1)
                    else:
                        pass

            await asyncio.sleep(1)
        else:
            pass
