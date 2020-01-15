import matplotlib
matplotlib.use('tkagg') # only way to render without an Xserver running
import matplotlib.pyplot as plt
from stats import x_value, y_value
import discord
import os
import time
from misc import standardize_struct_time

async def graph(message, client):

    #file_name = standardize_struct_time(time.localtime()) + ' ' + message.guild.name  + ' '
    file_name = (time.strftime('%Y%m%d %H%M', time.localtime()) + ' ' + message.guild.name \
                 + ' ')

    save_dir = os.path.join(os.getcwd(), file_name)

    image_extension = "stats.png"

    fname = save_dir + image_extension

    fmt = 'o-r' #MarkerLineColor
    plt.plot(x_value, y_value, fmt)
    plt.xlabel("Time")
    plt.ylabel("Messages sent")

    xticklabels = [str(i) for i in range(0, 2500, 200)]
    xticklocations = [i for i in range(0, 2500, 200)]
    plt.xticks(xticklocations, xticklabels)

    plt.grid()

    plt.title("Messages sent in the FireTrucks Discord Server on " + standardize_struct_time(time.localtime()))

    plt.savefig(fname)

    file = discord.File(fname, filename=fname)

    await message.channel.send(file=file)

