import discord 
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_message(ctx):
    badWords = ["dum"]
    hjamoArr = ["Hjamo", "hjamo", "Hjalmar", "hjalmar"]
    hjamoResp = ["Menar du den vansinniga grabben",
            "Menar du han med armarna",
            "Menar du chips-mannen",
            "Menar du han som som andas i micken",
            "Menar du sömntutan"
            ]
    for x in hjamoArr:
        if ctx.content.find(x) != -1 and str(ctx.author.name) != 'Ban-Hammer':
            theString = x + "? " + random.choice(hjamoResp) + "?"
            await ctx.channel.send(f'{theString}')
            break

    for y in badWords:
        if ctx.content.find(y) != -1:
            pic = discord.File('pictures/weirdChamp.jpg')
            await ctx.channel.send(file = pic)
            await ctx.channel.send("Märkligt sagt")
            break
    

    await bot.process_commands(ctx)


@bot.command()
async def decider(ctx, *, alternatives = None):
    arrWithAlternatives = alternatives.split(', ')
    if alternatives == None:
        await ctx.send('Syntax: ".decider alt1 alt2 alt3" you can use more or less alternatices than 3')
    else:
        await ctx.send(f'{random.choice(arrWithAlternatives)}')

@bot.command()
async def delete(ctx, number = 5):
    await ctx.channel.purge(limit = (number + 1))


@bot.command(pass_context = True)
async def users(ctx):
    members = bot.get_all_members()
    users = 0
    online = 0
    offline = 0
    other = 0
    for member in members:
        users += 1
        if str(member.status) == 'online':
            online += 1
        elif str(member.status) == 'offline':
            offline += 1
        else:
            other += 1
    
    await ctx.send(f'```Users on server: {users}\n  Online: {online}\n  Offline: {offline}\n  Other: {other}```')

@bot.command(pass_context = True)
async def activity(ctx, member : discord.Member):
    name = member.name
    activity = "is doing nothing"
    if member.activity:
        activityType = str(member.activity.type)
        temp = activityType.split('.')
        activityType = temp[1]
        if activityType == 'listening':
            activityType += " to"
        activity = str(member.activity.name)
        await ctx.send(f'{name} is {activityType} {activity}')
    else:
        await ctx.send(f'{name} {activity}')


@bot.command(pass_context = True)
async def activities(ctx):
    members = bot.get_all_members()
    serverActivities = {}

    for member in members:
        if str(member.status) != 'offline':
            activity = ""
            if not member.activity:
                activity = "Doing nothing"
            elif str(member.activity.name) == 'Custom Status' or str(member.activity.name) == 'with code | .halp / ub3r.bot':
                activity = "Custom Status"
            else:
                activity = member.activity.name
            
            if activity not in serverActivities:
                serverActivities[activity] = 1
            else:
                currentAmount = int(serverActivities[activity])
                newAmount = currentAmount + 1
                serverActivities[activity] = newAmount

    if len(serverActivities) == 0:
        finalString = "No activities are done right now"
    else:
        finalString = ""
        for x in serverActivities:
            finalString += x
            finalString += ": " + str(serverActivities[x])
            finalString += "\n"
        
    await ctx.send(f'```User activities on server\n{finalString}```')


bot.run('') #Enter bot token here
