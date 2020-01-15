import time

message_cache = {}

async def logger(message):
    file_name = "logs.txt"
    Time = time.strftime('%Y/%m/%d %H:%M', time.localtime())
    author = message.author
    content = message_cache[message.id]

    print("Message delete detected!")

    try:

        if message.id in message_cache:
            with open("logs.txt", "a") as logs:
                logs.write(f"{Time}\n "
                           f"{author}: {content}\n")

            print("Logging deleted messages...")

    except UnicodeEncodeError:

        #Functionality not supported for messages with emojis or embeds...
        '''
        stripped = str(content.strip(":"))
        with open("logs.txt", "a") as logs:
            logs.write(f"{Time}\n "
                       f"{author}: {stripped}\n")

            print("Logging stripped messages...")
        '''
        print("Message with emoji not logged...")

    if message.author == "Groovy#7254":
        pass