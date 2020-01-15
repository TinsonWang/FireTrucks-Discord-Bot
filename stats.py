import discord
import asyncio
import time

x_value = []
y_value = []

async def update_stats(client):
    await client.wait_until_ready()
    global messages, joined

    # This is the part that is looped
    # Until client is closed, this will loop
    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                time_stripped = time.strftime('%H%M', time.localtime()).lstrip("0")

                #Changed messages to client.messages and joined to client.joined to reflect the attributes we gave client during initialization -Tinson
                f.write(f"Time: {int(time_stripped)}, Messages: {client.messages}, Members joined: {client.joined}\n")

            # If we wanted to reset these to 0 each interval
            # messages = 0
            # joined = 0

            x_value.append(int(time_stripped))

            y_value.append(client.messages)

            # Write into the stats file every x seconds
            await asyncio.sleep(600)
        except Exception as e:
            print(e)

async def clear_stats(client):
    open("stats.txt", 'w').close()

async def clear_logs(client):
    open("logs.txt", 'w').close()