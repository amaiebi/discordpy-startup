import discord
from os import getenv
import random

random.seed(0)

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

    if message.content.startswith('!wsデッキ'):
    	deck = ['デレマス', 'バンドリ', 'ダカーポ', '虹ヶ咲8電源', '虹ヶ咲扉電源', '虹ヶ咲本枝']
    	deckLength = len(deck)
    	number = random. randrange(deckLength)
    	response = deck[number]
    	await message.channel.send(response)
         
    if message.content.startswith('!megami'):
    	megami = {"ユリナ", "サイネ", "ヒミカ", "トコヨ"}
    	response = random.sample(megami, 2)
    	await message.channel.send(response)
        
    if message.content.startswith('!tatsujin'):
    	megami_tatsujin = {"ユリナ", "サイネ", "ヒミカ", "トコヨ", "オボロ", "ユキヒ", "シンラ", "ハガネ", "チカゲ", "クルル", "サリヤ", "ライラ"}
    	response = random.sample(megami_tatsujin, 2)
    	await message.channel.send(response)        
        
        
token = getenv('DISCORD_BOT_TOKEN')
client.run(token)
