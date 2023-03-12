import discord
import os
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import lxml
from discord.ext import tasks
import asyncio
#import bot.py


intents = discord.Intents.default()
intents.all()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix='$', intents=intents)

client = discord.Client(intents = intents)
channel = client.get_channel(1084233131017633883)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


    
    
  
  

 #line 35 changed from client to bot for testing
""""@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
  
    print(f'Message {user_message} by {username} on {channel}')
  
    if message.author == client.user:
        return
  
    if channel == channel:
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')"""





intents = discord.Intents.default()
intents.all()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix='$', intents=intents)
DCB = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
          
"""@bot.command()
async def yourcommandnamehere(ctx):
    await ctx.send("random text")
#_______________________________________________"""

@bot.command()
async def repeat(ctx, *args):
    for arg in args:
        await ctx.send(arg)

@bot.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    #region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    #icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title = name + " Server Information",
        description = description,
        color=discord.Color.dark_red()
    )
    #embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    #embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
    print('pass')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


    
    
  
  

 #line 35 changed from client to bot for testing
""""@bot.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
  
    print(f'Message {user_message} by {username} on {channel}')
  
    if message.author == bot.user:
        return
  
    if channel == channel:
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}',reference=message)
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}',reference=message)
            await bot.process_commands(message)"""

bot.run(os.getenv('TOKEN'))

#client.run(os.getenv('TOKEN'))
#client.run(os.getenv('TOKEN'))

