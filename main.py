import discord, os, datetime, pytz, translate

ADMIN = 'typedecker'
ADMIN_DISCRIMINATOR = '7906'

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
    if defaulter.name != ADMIN and defaulter.discriminator != ADMIN_DISCRIMINATOR :
        print(defaulter.roles)
        await defaulter.edit(roles = [])
        print(defaulter.roles)
        # for role in defaulter.roles :
        #     print(role.name, role)
        #     if role.name != '@everyone' :
        #         await defaulter.remove_roles(role)
        await channel.guild.channels[0].send(defaulter.name + ' tried to delete a channel he is a clan betrayer! All his roles have been removed and the ADMIN has been notified.')
    
        # try :
        #     msg_history = await delete_entry.before.channel.history()
        #     new_channel = await channel.guild.create_text_channel(channel.name, channel.overwrites, channel.category, channel.position, channel.topic, channel.slowmode_delay, channel.nsfw, channel.reason)
        #     for msg in msg_history :
        #         await new_channel.send(msg.author + ' : ' + msg.content)
        #     await new_channel.send('All messages of the deleted channel have been restored.')
        # except :
        #     await channel.guild.channels[0].send('Unfortunately the deleted channel could not be restored. I am sorry I tried my best to get it back!')
        #     pass
        
        archive_permissions = None
        for category in channel.guild.categories :
                if category.name == 'CHANNEL ARCHIVES' :
                    archive_permissions = category.permissions
        
        # PRIMARY CHANNEL RESTORATION
        restored = False
        for channel_ in channel.guild.channels :
            if channel_.name == channel.name + '_ARCHIVE' :
                if archive_permissions != None :
                    if archive_permissions == channel_.permissions :
                        pass
                    else :
                        continue
                restored_channel = await channel_.clone(channel_.name[ : -8] + '_RESTORED')
                restored_channel.permissions = discord.Permissions(send_messages = False, read_messages = True)
                await restored_channel.send('@everyone THE CHANNEL HAS BEEN RESTORED.')
                restored = True
                break
            else :
                continue
        if not restored :
            await channel.guild.channels[0].send('Unfortunately the deleted channel could not be restored. I am sorry I tried my best to get it back!')
        
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
    print('MESSAGE AUTHOR NAME:', message.author.name, 'MESSAGE AUTHOR ID:', message.author.id, 'MESSAGE AUTHOR DISCRIMINATOR!', message.author.discriminator)
    if message.author == client.user :
        return
    
    if message.author.name == ADMIN and message.author.discriminator == ADMIN_DISCRIMINATOR :
        print('ADMIN KA JADOO!!!!')
        if message.content.lower().startswith('$$type bot the following players did not attack ') :
            for user in message.mentions :
                if user.dm_channel == None :
                    await user.create_dm()
                
                await user.dm_channel.send('Its a request to use your war attack second/both as soon as possible. If you feel like the targets left are too hard its ok, still atleast use your attack and try to claim targets from before for next war.')
                await user.dm_channel.send('NOTE: On not using your attack, based on how loyal you are in the clan you might have to give a reason for addition in next war.')
            pass
        elif message.content.lower() == '$$type bot archive all' :
            archive_permissions = None
            for category in message.guild.categories :
                    if category.name == 'CHANNEL ARCHIVES' :
                        archive_permissions = category.permissions
            for channel in message.guild.channels :
                if archive_permissions == None :
                    archive_permissions = channel.permissions
                archive_channel = await channel.clone(name = channel.name + '_ARCHIVE', reason = 'ARCHIVING THE CHANNEL AS PER INSTRUCTIONS FROM ADMIN.')
                archive_channel.permissions = archive_permissions
        elif message.content.lower() == '$$type bot restore all' :
            archive_permissions = None
            for category in message.guild.categories :
                    if category.name == 'CHANNEL ARCHIVES' :
                        archive_permissions = category.permissions
            for channel in message.guild.channels :
                if channel.name[-8 : ] == '_ARCHIVE' :
                    if archive_permissions != None :
                        if archive_permissions == channel.permissions :
                            pass
                        else :
                            continue
                    restored_channel = await channel.clone(channel.name[ : -8] + '_RESTORED')
                    restored_channel.permissions = discord.Permissions(send_messages = False, read_messages = True)
                    await restored_channel.send('@everyone THE CHANNEL HAS BEEN RESTORED.')
                else :
                    continue
        elif message.content.lower().startswith('$$type bot primary archive ') :
            content = message.content
            target_channel = content[content.index('[') + 1, content.index(']')]
            archive_permissions = None
            for category in message.guild.categories :
                    if category.name == 'CHANNEL ARCHIVES' :
                        archive_permissions = category.permissions
            archived = False
            for channel in message.guild.channels :
                if channel.name == target_channel :
                    if archive_permissions == None :
                        archive_permissions = channel.permissions
                    archive_channel = await channel.clone(name = channel.name + '_ARCHIVE', reason = 'ARCHIVING THE CHANNEL AS PER INSTRUCTIONS FROM ADMIN.')
                    archive_channel.permissions = archive_permissions
                    archived = True
                    break
                continue
            if archived :
                await message.guild.channels[0].send('The channel was archived succesfully!')
            else :
                await message.guild.channels[0].send('The channel could not be archived.')
        elif message.content.lower().startswith('$$type bot primary restore ') :
            content = message.content
            target_channel = content[content.index('[') + 1, content.index(']')]
            archive_permissions = None
            for category in message.guild.categories :
                    if category.name == 'CHANNEL ARCHIVES' :
                        archive_permissions = category.permissions
            restored = False
            for channel in message.guild.channels :
                if channel.name == target_channel + '_ARCHIVE' :
                    if archive_permissions != None :
                        if archive_permissions == channel.permissions :
                            pass
                        else :
                            continue
                    restored_channel = await channel.clone(channel.name[ : -8] + '_RESTORED')
                    restored_channel.permissions = discord.Permissions(send_messages = False, read_messages = True)
                    await restored_channel.send('@everyone THE CHANNEL HAS BEEN RESTORED.')
                    restored = True
                    break
                else :
                    continue
            if not restored :
                await message.guild.channels[0].send('The channel could not be restored.(ADMIN KNOWS WHY, BUT ITS A SECRET.)')
        elif message.content.lower().startswith('$$type bot delete primary archive ') :
            content = message.content
            target_channel = content[content.index('[') + 1, content.index(']')]
            archive_permissions = None
            for category in message.guild.categories :
                    if category.name == 'CHANNEL ARCHIVES' :
                        archive_permissions = category.permissions
            deleted = False
            for channel in message.guild.channels :
                if channel.name == target_channel + '_ARCHIVE' :
                    if archive_permissions != None :
                        if archive_permissions == channel.permissions :
                            pass
                        else :
                            continue
                    await channel.delete()
                    deleted = True
                    break
                else :
                    continue
            if not deleted :
                await message.guild.channels[0].send('The channel archive could not be deleted.(ADMIN KNOWS WHY, BUT ITS A SECRET.)')
        elif message.content.lower().startswith('$$type bot promote ') :
            # args = message.content[19 : ]
            # target = message.mentions[0]
            # role_name = args.split()[1].strip()
            content = message.content
            # args = [k.strip() for k in content.split(',')]
            target = message.mentions[0]
            role_name = content[content.index('[') + 1, content.index(']')]
            promote_role = None
            for role in message.guild.roles :
                if role.name == role_name :
                    promote_role = role
                    break
            target_roles = target.roles
            if not target_roles.__contains__(promote_role) :
                target_roles.append(promote_role)
                message.mentions[0].edit(role = target_roles)
                message.channel.send('Congratulations ' + target.name + '! You have been promoted to ' + promote_role.name)
                if target.dm_channel == None :
                    target.create_dm()
                target.dm_channel.send('Congratulations ' + target.name + '! You have been promoted to ' + promote_role.name)
            else :
                message.channel.send('The member already has that role.')
        elif message.content.lower().startswith('$$type bot demote ') :
            content = message.content
            target = message.mentions[0]
            role_name = content[content.index('[') + 1, content.index(']')]
            demote_role = None
            for role in message.guild.roles :
                if role.name == role_name :
                    demote_role = role
                    break
            target_roles = target.roles
            if target_roles.__contains__(demote_role) :
                target_roles.remove(promote_role)
                message.mentions[0].edit(role = target_roles)
                message.channel.send('So unfortunate ' + target.name + '! You have been demoted from ' + demote_role.name)
                if target.dm_channel == None :
                    target.create_dm()
                message.channel.send('So unfortunate ' + target.name + '! You have been demoted from ' + demote_role.name)
            else :
                message.channel.send('The member already does not have that role.')
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
    
    if message.content.lower().startswith('$$time ') :
        content = message.content
        try :
            tz = content[content.index('[') + 1 : content.index(']')]
            await message.channel.send('The time in this timezone is ' + str(datetime.datetime.now(pytz.timezone(tz))))
        except :
            await message.channel.send('The timezone could not be found.')
    
    if message.content.lower().startswith('$$translate ') :
        content = message.content
        args = [k.strip() for k in content[12 : ].split(',')]
        from_lang = args[0]
        to_lang = args[1]
        sample = args[2]
        sample = sample[sample.index('[') + 1 : sample.index(']')]
        try :
            translator = translate.Translator(from_lang = from_lang, to_lang = to_lang)
            await message.channel.send('TRANSLATED: [' + translator.translate(sample) + ']')
        except :
            await message.channel.send('Couldn\'t translate due to some error. Please try again.')
        

client.run(os.environ['BOT_TOKEN'])
