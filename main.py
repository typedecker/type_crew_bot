import discord, os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    abuses = ['fuck', 'dick', 'ass']
    for abuse in abuses :
        if message.content.lower().__contains__(abuse) :
            await message.delete() # DELETES MSGS WITH ABUSES.
            await message.channel.send('No abusing' + message.author + 'maybe you did not read our clan rules properly. Make sure to do so you can type \"$$CLAN RULES\" as a command and I will explain them to ya!')

    if message.content.lower().startswith('hello type bot'):
        await message.channel.send('Hello!')
    
    if message.content.lower() == '$$type bot prep day started' :
        await message.channel.send('Friends War prep day has started!')
        await message.channel.send('> Please claim your targets and also please only claim those targets that have not already been claimed by someone else.')
        await message.channel.send('> Stealing of targets on war day is not allowed, so if you do not claim a target you\'ll automatically become a part of the cleanup crew.')
        await message.channel.send('> If you are doing cleanup this war, make sure to inform it to me once on discord or on clan chat.')
        await message.channel.send('> I will be filling war defense ccs soon. If you wanna help fill them(No Force), then for 30+ cc space e drags(with loons if needed), for 40+ e drags with baby ds, for 20+ drags(with loons if needed) for 10+ baby ds')
        await message.channel.send('Thanks! Good luck for war!')
    
    if message.content.lower() == '$$type bot war day started' :
        await message.channel.send('Friends War day has started!')
        await message.channel.send('> Please use both your attacks.')
        await message.channel.send('> No target stealing!')
        await message.channel.send('> If you want to attack on someone else\'s target make sure to ask them and only attack if they allow or if they have not attacked till war end.')
        await message.channel.send('> If you could only claim one target or only claimed one, then use the other one for cleanup.')
        await message.channel.send('> Those part of cleanup crew can help with cleanup near war end, but make sure you do attack by the end and do not forget to do so.')
        await message.channel.send('Thanks! Good luck for war!')

    if message.content == '$$CLAN RULES' :
        await message.channel.send('Welcome to the TYPE CREW!')
        await message.channel.send('> Co is earned through loyalty and Activeness in War.')
        await message.channel.send('> NO ABUSES!!!(except for when joking...)')
        await message.channel.send('> Do not ask for promotions yourself you will get them when you are eligible to!')
        await message.channel.send('> If you are found inactive without any reason given, you will be kicked.')
        await message.channel.send('> Wars are optional but CLAN GAMES are mandatory.')
        await message.channel.send('> Only Active, Loyal members will be taken in CWL.')
        await message.channel.send('> No HOPPERS! You join, you stay or else you go away!')
        await message.channel.send('# TechnoSupport : Our clan supports techno in his fight against cancer!')

client.run(os.environ['BOT_TOKEN'])
