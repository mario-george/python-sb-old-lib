import os
import discord
import pyfiglet as pyfi
import random
from discord.ext import  commands
from keep_alive import keep_alive
ids = []
import time
#if Cloudfair is blocking --type kill 1 in shell

prefix="!"
list=["http", "www", ".com", ".mx", ".org", ".net", ".co.uk", ".jp", ".ch", ".info", ".me", ".mobi", ".us", ".biz", ".ca", ".ws", ".ag", 
		".com.co", ".net.co", ".com.ag", ".net.ag", ".it", ".fr", ".tv", ".am", ".asia", ".at", ".be", ".cc", ".de", ".es", ".com.es", ".eu", 
		".fm", ".in", ".tk", ".com.mx", ".nl", ".nu", ".tw", ".vg",  "buy", "free", "dating", "money", "dollars", 
		"payment", "website", "games", "toys", "poker", "cheap"]

intents = discord.Intents.all()
intents.members=True
client = commands.Bot(command_prefix='!',intents=intents,self_bot=True)
@client.event
async def on_ready():
  print("Bot is Ready")
  print("-----------------------------------------------------")
@client.event
async def on_message(message):

  print(message.content)
   # await message.author.send("Hello")
  print("on_messageinvoked")
  


@client.event
async def on_member_join(member):
  channel=client.get_channel(1008440420952461466)
  print(member)
  await channel.send(f"Hello {member.mention}")
  await channel.send(member)
  await member.send(f"Hello {member.mention}")

@client.event
async def on_member_remove(member):
  channel=client.get_channel(1008440420952461466)
  print(member)
  await channel.send(f"Bye{member.mention}")

  await member.send(f"Bye +{member.mention}")
  print("Bye")

@client.command()
async def ping(ctx):
  await ctx.send("Pong")
#await the function you're in gets suspended while whatever you asked to wait on happens,
@client.command()
async def embed(ctx): 
  embed=discord.Embed(text="dog",description="we love dogs",url="www.google.com",color=0xFFF000)
  await ctx.send(embed.embed)
#await the function you're in gets suspended while whatever you asked to wait on happens,

token = os.environ['token']
keep_alive()
#keep the webserver alive
client.run(token,bot=False)
