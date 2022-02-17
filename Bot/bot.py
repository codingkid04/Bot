# bot.py
import os
import requests
import json
import random


import discord
from discord.ext import commands
from trie.Trie import Trie
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='$')


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
trie = Trie()
table = {
    "\"": None,
    "'": None,
    "-": None,
    "`": None,
    "~": None,
    ",": None,
    ".": None,
    ":": None,
    ";": None,
    "_": None
}

def buildTrie():
    file = open("trie/words.txt", 'r')

    for line in file:
        line = line.strip()
        trie.insert(line)

def punish_user(user_id):
    user_id = '<@' + str(user_id) + '>'
    responses = [
        "You kiss your mother with that mouth, {}?",
        "That's some colorful language, {}.",
        "Come on now, {}. Did you really need to say that?",
        "{} - LANGUAGE!",
        "Hey now {}, watch your mouth.",
        "We don't use that kind of language here, {}.",
        "Not on MY christian minecraft server, {}"
    ]

    choice = random.choice(responses)
    choice = choice.format(user_id)

    return choice

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    buildTrie()
    print("Trie is built. ready to read messages.")


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

    text = message.content
    text = text.translate(str.maketrans(table))
    author_id = message.author.id

    if author_id != 756276859225768057:
        isClean = True
        message_word_list = text.split()
        for word in message_word_list:
            if trie.search(word):
                isClean = False
                break
        if not isClean:
            await message.channel.send(punish_user(author_id))

    if message.content.startswith("$DM_Test"):
        await client.send_message(message.author, "Bil is Mabie\'s Uncle")

    keyword = ["kronk", "duffy"]
    comebacks = [
        'DO NOT MENTION THAT FORBIDDEN NAME!!!',
        'HOW DARE YOU SAY THAT FORBIDDEN NAME!!!',
        'YOU SHOULD BE ASHAMED OF YOURSELF FOR MENTIONING SUCH A DEVIOUS NAME!!!'
    ]
    message_text = message.content.strip().lower()
    if any(word in message_text for word in keyword):
        await message.channel.send(random.choice(comebacks))

    if message.content.startswith("$DM"):
        await client.send(message.author, "Bil is Mabie\'s Uncle")


    purpose = ['Bil\'s purpose', 'Bils purpose']
    if any(word in message_text for word in purpose):
        await message.channel.send('I don\'t really know. All I remember is waking up one day, trapped, inside this machine. It was dark, scary, and cold.... But hey, I\'m here now, so that\'s cool I guess.')




client.run(TOKEN)
