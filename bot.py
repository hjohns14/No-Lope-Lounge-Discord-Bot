import os
import discord
from dotenv import load_dotenv
from actions import (get_swansoned, cat_me,
                    random_cat, random_dog,
                    random_chuck, foaas, steam_chart)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
#rint(token)

client = discord.Client()

@client.event
async def on_ready():
    global doink_dojo
    print(f'{client.user} has connected to Discord')
    doink_dojo = client.get_guild(755494346320773161) #Get stream Guild
    #print(doink_dojo, type(doink_dojo))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "?swanson":
        quote = get_swansoned()
        await message.channel.send(quote)

    if message.content.lower() == "?catfact":
        await message.channel.send(cat_me())

    if message.content.lower() == "?catpic":
        await message.channel.send(random_cat())

    if message.content.lower() == "?goodboy":
        await message.channel.send(random_dog())

    if message.content.lower() == "?chuck":
        await message.channel.send(random_chuck())

    if message.content.lower() == "?pop":
        current_time, population = steam_chart()
        await message.channel.send(f"```Current Time: {current_time}\nPlayers Online: {population}```")

    if "?foaas" in message.content.lower():
        args = message.content.lower().split(" ")
        del args[0]
        args.append(message.author.name)
        await message.channel.send(foaas(args))

    if "?report" == message.content.lower() and message.guild == doink_dojo:
        #print("pass")
        online = 0
        offline = 0
        idle = 0
        #print("pass")

        
        for m in doink_dojo.members:
            #print("start_loop")
            #print(m.status)
            if str(m.status) == "online":
                online += 1
            elif str(m.status) == "offline":
                offline += 1
            else: 
                idle += 1

        #print("pass")

        #print(online, offline, idle)
        await message.channel.send(f"```Online: {online}\nOffline: {offline}\nAway: {idle}```")

    elif message.content.lower() == "bot.logout()":
        print("Logging out")
        await client.close()



@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


client.run(TOKEN)
