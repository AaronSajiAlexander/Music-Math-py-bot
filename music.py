import discord #to use FFmpegOpusAudio.
from discord.ext import commands 
import youtube_dl #youtube related info and downloading audio from the youtube videos. 


class music(commands.Cog):
  def __init__(self,client):
    self.client = client 


  @commands.command()
  async def join(self,ctx): #join command so that the both would join the music channel. For example type ?join for the bot to join the voice channel
    if ctx.author.voice is None: #if user not in a voice channel
      await ctx.send("You are not in a voice channel")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None: #if bot not in voice channel
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel) #moves the bot to the channel in which the user is present.


  @commands.command()
  async def disconnect(self,ctx):
    await ctx.voice_client.disconnect() #disconnects the bot from the voice channel

  @commands.command()
  async def play(self,ctx,url):
    ctx.voice_client.stop() # if any music is already running , it stops it .
    FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'} #ffmpeg handles the streaming in discord . the preferences here are standard for streaming.
    YDL_OPTIONS = {'format':"bestaudio"} #to make sure the audio is in the best format
    vc = ctx.voice_client
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl: #preparing to stream the audio 
      info = ydl.extract_info(url , download = False)
      url2 = info['formats'][0]['url'] 
      source = await discord.FFmpegOpusAudio.from_probe(url2 , **FFMPEG_OPTIONS) # creating a stream to play audio 
      vc.play(source)


  @commands.command()
  async def pause(self,ctx):
    await ctx.voice_client.pause() #pauses the music
    await ctx.send("Paused ⏸️")   

  @commands.command()
  async def resume(self,ctx):
    await ctx.voice_client.resume() #resumes the music
    await ctx.send("Resumed ⏯️")     


def setup(client):
  client.add_cog(music(client))

