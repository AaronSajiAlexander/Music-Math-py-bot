import discord #to use discord.Intents.all() to choose which events the bot receives
import os #for mapping object that represent user's environment variable
from discord.ext import commands #to define commands and invoke functions using them
import math #for using math.sqrt()
import random #for using random.randint()
from keep_alive import keep_alive #the web server file which runs in flask
import music #the file the contains the code for music commands

cogs = [music] #putting music in the cogs list 

client = commands.Bot(command_prefix = '?',intents = discord.Intents.all()) #initiate the bot


for i in range(len(cogs)):
  cogs[i].setup(client) #invoking setup() function in music.py
 

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
async def add(ctx ,x:float ,y:float):  # for example, type ?add 10 20 for this function to get invoked
  res = Add(x,y)
  await ctx.send(res)
  

@client.command()
async def sub(ctx,x:float ,y:float): # for example, type ?sub 10 20 for this function to get invoked
  res = Sub(x,y)
  await ctx.send(res)

  

@client.command()
async def div(ctx,x:float ,y:float): # for example, type ?div 10 2 for this function to get invoked
  res = Div(x,y)
  await ctx.send(res)
  

@client.command()
async def mul(ctx,x:float ,y:float): # for example, type ?mul 10 5 for this function to get invoked
  res = Mult(x,y)
  await ctx.send(res)
  

@client.command()
async def sqrt(ctx,x:float): # for example, type ?sqrt 49 for this function to get invoked
  res = Sqrt(x)
  await ctx.send(res)
  

@client.command()
async def rando(ctx,x:int ,y:int): # for example, type ?rando 10 20 for this function to get invoked
  res = Rando(x,y)
  await ctx.send(res) 


my_secret = os.environ['TOKEN'] # storing the bot key in a variable called my_secret 
keep_alive() # invokes the function keep_alive() in keep_alive.py which has the web page
client.run(my_secret) #running the bot
