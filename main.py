import discord, os

ADMIN = 'typedecker'
ADMIN_ID = 7906

intents = discord.Intents(guilds = True, dm_messages = True, members = True, messages = True, guild_messages = True)
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member) :
    if member.dm_channel == None :
        await member.create_dm()
    await member.dm_channel.send('Hi! Welcome to the TYPE CREW OFFICIAL DISCORD SERVER!, our admins will verify you as soon as they get online. Once verified you can view the channels! Please note the following clan rules(You can request to view them later by writing $$CLAN RULES TO ME) -:')
    await member.dm_channel.send('Welcome to the TYPE CREW!')
    await member.dm_channel.send('> Co is earned through loyalty and Activeness in War.')
    await member.dm_channel.send('> NO ABUSES!!!(except for when joking...)')
    await member.dm_channel.send('> Do not ask for promotions yourself you will get them when you are eligible to!')
    await member.dm_channel.send('> If you are found inactive without any reason given, you will be kicked.')
    await member.dm_channel.send('> Wars are optional but CLAN GAMES are mandatory.')
    await member.dm_channel.send('> Only Active, Loyal members will be taken in CWL.')
    await member.dm_channel.send('> No HOPPERS! You join, you stay or else you go away!')
    await member.dm_channel.send('# TechnoSupport : Our clan supports techno in his fight against cancer!')
    return

@client.event
async def on_guild_channel_delete(channel) :
    # delete_entries = 
    # delete_entry = [entry for entry in client.get_guild(channel.guild.id).audit_logs(action = discord.AuditLogAction.channel_delete)][-1]
    
    entries = await client.get_guild(channel.guild.id).audit_logs(action = discord.AuditLogAction.channel_delete).flatten()
    print(type(entries), entries)
    delete_entry = entries[0]
    print(delete_entry)
    # print('{0.user} banned {0.target}'.format(entry))
    # channel.send(str(delete_entry))
    defaulter = delete_entry.user
    if defaulter.name != ADMIN and defaulter.id != ADMIN_ID :
        print(defaulter.roles)
        await defaulter.edit(roles = [])
        print(defaulter.roles)
        # for role in defaulter.roles :
        #     print(role.name, role)
        #     if role.name != '@everyone' :
        #         await defaulter.remove_roles(role)
        await channel.guild.channels[0].send(defaulter.name + ' tried to delete a channel he is a clan betrayer! All his roles have been removed and the ADMIN has been notified.')
    
    try :
        msg_history = await delete_entry.before.channel.history()
        new_channel = await channel.guild.create_text_channel(channel.name, channel.overwrites, channel.category, channel.position, channel.topic, channel.slowmode_delay, channel.nsfw, channel.reason)
        for msg in msg_history :
            await new_channel.send(msg.author + ' : ' + msg.content)
        await new_channel.send('All messages of the deleted channel have been restored.')
    except :
        await channel.guild.channels[0].send('Unfortunately the deleted channel could not be restored. I am sorry I tried my best to get it back!')
        pass
    
    if defaulter.dm_channel == None :
        await defaulter.create_dm()
    
    await defaulter.dm_channel.send('You are a CLAN BETRAYER!')
    await defaulter.dm_channel.send('You fool, you really thought no one was there to see what you were tryna do?')
    await defaulter.dm_channel.send('Till the day I exist, I will not let anyone harm my server.')
    await defaulter.dm_channel.send('The channel that was deleted has been restored back to exactly how it was, so your efforts totally went into ruins!')
    await defaulter.dm_channel.send('GET BETTER YOU FOOL, WE AND OUR SECURITY SYSTEMS ARE WAY ABOVE YOUR MORAL UNDERSTANDING AND EXISTENCE!')
    await defaulter.dm_channel.send('Be happy, you still are in the server, I would have banned you, but ADMIN is a really nice guy he wants to talk before letting you go away.')
    return

@client.event
async def on_message(message):
    if message.author == client.user :
        return
    
    if message.author.name == ADMIN and message.author.id == ADMIN_ID and message.content.lower().startswith('$$type bot the following players did not attack ') :
        # SEND THEM DMS
        pass
    
    abuses = ['fuck', 'dick']
    for abuse in abuses :
        if message.content.lower().__contains__(abuse) :
            await message.channel.send('No abusing ' + message.author.name + ' maybe you did not read our clan rules properly. Make sure to do so you can type \"$$CLAN RULES\" as a command and I will explain them to ya!')
            await message.delete() # DELETES MSGS WITH ABUSES.

    if message.content.lower().startswith('hello type bot'):
        await message.channel.send('Hello!')
    
    if message.content.lower() == '$$who is the champ?' :
        await message.channel.send('Obviously it is deadshot bro.')
    
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
