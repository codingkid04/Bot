# bot.py
import os
import requests
import json
import random


import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hey {member.name}, welcome to the **CAPSOC Discord Server!** Here you can find all kinds of stuff, but before you do anything, please take time to look into our **Rules** channel and get familiar with it. If you have any questions or concerns, please contact the moderators of this sever!'
    )



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    keyword = ["kronk", "duffy"]
    comebacks = [
        'DO NOT MENTION THAT FORBIDDEN NAME!!!',
        'HOW DARE YOU SAY THAT FORBIDDEN NAME!!!',
        'YOU SHOULD BE ASHAMED OF YOURSELF FOR MENTIONING SUCH A DEVIOUS NAME!!!'
    ]
    message_text = message.content.strip().lower()
    if any(word in message_text for word in keyword):
        await message.channel.send(random.choice(comebacks))


    purpose = ['purpose', 'Purpose', 'Bil\'s purpose']
    if any(word in message_text for word in purpose):
        await message.channel.send('I don\'t really know. All I remember is waking up one day, trapped, inside this machine. It was dark, scary, and cold.... But hey, I\'m here now, so that\'s cool I guess.')





client.run(TOKEN)
