import discord
import os
from discord.ext import commands
import math
import random
from keep_alive import keep_alive
import music

cogs = [music]

client = commands.Bot(command_prefix = '?',intents = discord.Intents.all())


for i in range(len(cogs)):
  cogs[i].setup(client)
 

def Sub(x: float , y: float):
  return x-y


def Add(x: float , y: float):
  return x+y


def Mult(x:float , y:float):
  return x*y

def Div(x:float , y:float):
  return x/y


def Sqrt(x:float):
  return math.sqrt(x)  


def Rando(x:int , y:int):
  return random.randint(x,y)  



@client.command()
async def add(ctx ,x:float ,y:float):
  res = Add(x,y)
  await ctx.send(res)
  

@client.command()
async def sub(ctx,x:float ,y:float):
  res = Sub(x,y)
  await ctx.send(res)

  

@client.command()
async def div(ctx,x:float ,y:float):
  res = Div(x,y)
  await ctx.send(res)
  

@client.command()
async def mul(ctx,x:float ,y:float):
  res = Mult(x,y)
  await ctx.send(res)
  

@client.command()
async def sqrt(ctx,x:float):
  res = Sqrt(x)
  await ctx.send(res)
  

@client.command()
async def rando(ctx,x:int ,y:int):
  res = Rando(x,y)
  await ctx.send(res) 


my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)
