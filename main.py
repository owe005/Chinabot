import discord #discord
#import os
import pytz #chinatime
import random
import string
#import glob
import requests, json
#import matplotlib.pyplot as plt
import time
from googletrans import Translator
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime #chinatime
from random import choice

client = discord.Client()
status = cycle(["Surveillance Simulator", "Assassinating Defectors 2", "Hearts of Iron IV as Xi Jinping"])

@client.event
async def on_ready():
  change_status.start()
  print("Chinese Embassy is online and ready")

@tasks.loop(seconds=300)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_message(message):
  var = str(message.content)
  author = str(message.author)
  channel = str(message.channel)

  if author == "Magvy#0852":
        await message.add_reaction("🇨🇳")

  if message.author.bot == True:
      return

  if channel == "grabrantastranark":
      return

### Translations ###

  if channel == "chinese-translation":
      translator = Translator()
      results = translator.translate(var, dest='zh-cn')
      await message.channel.send(results.text)

  if channel == "english-translation":
      translator2 = Translator()
      results2 = translator2.translate(var, dest='en')
      await message.channel.send(results2.text)

  if channel == "norwegian-translation":
      translator3 = Translator()
      results3 = translator3.translate(var, dest='no')
      await message.channel.send(results3.text)

### End Translations ###

  if message.content.startswith('c.lightshot'):
      randomurlString = string.ascii_lowercase + string.digits
      randomizing = ''.join(random.choice(randomurlString) for i in range(6))
      url = "https://prnt.sc/" + str(randomizing)
      await message.channel.send(url)

  if message.content.startswith('c.weather '):
      msg = message.content[10:]
      city_name = str(msg)
      complete_url = base_url + "appid=" + api_key + "&q=" + city_name
      response = requests.get(complete_url)
      x = response.json()

      if x["cod"] != "404":
          y = x["main"]
          current_temperature = y["temp"]
          current_temperature = current_temperature - 273.15
          current_temperature = round(current_temperature, 2)
          z = x["weather"]
          weather_description = z[0]["description"]
          toSend = "Temperature = " + str(current_temperature) + "℃ \ndescription = " + weather_description
          await message.channel.send(toSend)

      else:
          await message.channel.send("Place not found")

  #if message.content.startswith('c.function '):
      #msg = int((message.content[11:]))
      #x = np.linspace(-5,5,100)
      #y = x**msg
      #plt.plot(x,y)
      #plt.legend(["x^"+str(msg)])

      #figure = "figures/figure"+str(random.sample(range(100000), 1)) +".jpg"
      #plt.savefig(figure)
      #plt.close()
      #await message.channel.send(file=discord.File(figure))

  if message.content.startswith("c.flipcoin"):
    deter = [1, 0]
    if random.choice(deter) == 1:
        embedVar2 = discord.Embed(title="Heads!", description="You rolled heads bro", color=0xff0000)
        embedVar2.set_thumbnail(url="https://www.pngkey.com/png/full/146-1464786_400px-circle-quarter-heads-side-of-coin.png")
        await message.channel.send(embed=embedVar2)
    else:
        embedVar3 = discord.Embed(title="Tails!", description="You rolled tails bro", color=0xff0000)
        embedVar3.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
        await message.channel.send(embed=embedVar3)

  if message.content.startswith('c.chinatime'):
    asia_time = pytz.timezone('Asia/Shanghai')
    country_time = datetime.now(asia_time)
    time = country_time.strftime("%H:%M:%S")
    china_time = "Currently it is " + time + " in China"
    await message.channel.send(china_time)


  ###
client.run(TOKEN)
