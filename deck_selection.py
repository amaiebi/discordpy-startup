import discord
from os import getenv
import random

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('/wsデッキ'):
    	deck = ['デレマス', 'バンドリ', 'ダカーポ', '虹ヶ咲8電源', '虹ヶ咲扉電源', '虹ヶ咲本枝']
    	deckLength = len(deck)
    	number = random. randrange(deckLength)
    	response = deck[number]
    	await message.channel.send(response)

token = getenv('DISCORD_BOT_TOKEN')
client.run(token)