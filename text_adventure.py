import discord
import time

def read_text_adventure_test():
    with open("text_adventure_1", "r") as t:
        section1 = ''
        section2 = ''
        section3 = ''
        section4 = ''
        section5 = ''
        for i in range(1, 18):
            section1 += t.readline()
        for i in range(17, 36):
            section2 += t.readline()
        for i in range(36, 57):
            section3 += t.readline()
        for i in range(57, 76):
            section4 += t.readline()
        for i in range(76, 95):
            section5 += t.readline()
        return section1, section2, section3, section4, section5


async def text_adventure(message):
    player = message.author
    section1, section2, section3, section4, section5 = read_text_adventure_test()

    await message.channel.send(section1)
    # The input() function only takes user input in the CONSOLE...not from the actual Discord Server itself!
    choice = input("Please enter a number: ")

    while choice != "1" and choice != "2":
        await message.channel.send("Response not recognized. Please enter a valid number")
        time.sleep(1)
        choice = input("Please enter a number: ")

    if choice == "1":
        await message.channel.send(str(player) + " has entered " + choice + " into the command terminal. \n...............")
        time.sleep(1)
        await message.channel.send(section2)
        choice = input("Please enter a number: ")

    elif choice == "2":
        await message.channel.send(str(player) + " has entered " + choice + " into the command terminal. \n...............")
        time.sleep(1)
        await message.channel.send(section3)
        choice = input("Please enter a number: ")

        while choice != "1" and choice != "2":
            await message.channel.send("Response not recognized. Please enter a valid number")
            time.sleep(1)
            choice = input("Please enter a number: ")

        if choice == "1":
            await message.channel.send(str(player) + " has entered " + choice + " into the command terminal. \n...............")
            time.sleep(1)
            await message.channel.send(section2)
            choice = input("Please enter a number: ")

        if choice == "2":
            await message.channel.send(str(player) + " has entered " + choice + " into the command terminal. \n...............")
            time.sleep(1)
            await message.channel.send(section4)
            choice = input("Please enter a number: ")

            while choice != "1" and choice != "2":
                await message.channel.send("Response not recognized. Please enter a valid number")
                time.sleep(1)
                choice = input("Please enter a number: ")

            if choice == "1":
                await message.channel.send(str(player) + " has entered " + choice + " into the command terminal. \n...............")
                time.sleep(1)
                await message.channel.send(section2)
                choice = input("Please enter a number: ")

            if choice == "2":
                await message.channel.send(str(player) + " has entered " + choice + " into the command terminal. \n...............")
                time.sleep(1)
                await message.channel.send(section5)
                choice = input("Please enter a number: ")


    #elif type(input) != "class 'int'":
        #await message.channel.send("Input not recognized - please try again.")
        #await message.channel.send(section1)
