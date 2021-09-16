import discord, os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('hello type bot'):
        await message.channel.send('Hello!')

    if message.content == '$$CLAN RULES' :
        await message.channel.send('Lol I just joined. >U<')

client.run(os.environ['BOT_TOKEN'])
