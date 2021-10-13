import discord
import os
from datetime import datetime
import pytz
import random

##China fact setup##
with open('facts.txt') as f:
  lines = f.readlines()
  random_int = random.randint(0,len(lines)-1)
  randomFact = lines[random_int]

with open('importantFacts.txt') as s:
  lines2 = s.readlines()
  random_int_2 = random.randint(0, len(lines2)-1)
  realFact = lines2[random_int_2]
#####################

client = discord.Client()

@client.event
async def on_ready():
  print("China Embassy is online and ready")


@client.event
async def on_message(message):

  if message.author == client.user:
    return

  if message.content.startswith('c.about'):
        embedVar = discord.Embed(title="Who am I?", description="I am a representative of the People's Republic of China acting on the interests of the greatest country on Earth.", color=0xff0000)

        embedVar.add_field(name="Available Commands", value = "These are the available commands that the People's Republic of China has allowed me to reveal: \n \n c.about \n c.time \n c.realfact \n c.funfact \n \n", inline=False)

        embedVar.set_footer(text="All non-citizens of China are subject to voluntarily labour within our labour-camps within due date. \n \nAuthor: Ole Westby")

        embedVar.set_thumbnail(url="https://cdn.pixabay.com/photo/2020/04/04/11/45/flag-5001937_960_720.jpg")
        await message.channel.send(embed=embedVar)

  if message.content.startswith("c.funfact"):
    await message.channel.send(randomFact)

  if message.content.startswith("c.realfact"):
    await message.channel.send(realFact)

  if 'based' in message.content:
    await message.channel.send("based on what?")

  if 'based on what' in message.content:
    await message.channel.send("your mom")

  if message.content.startswith('c.time'):
    asia_time = pytz.timezone('Asia/Shanghai')
    country_time = datetime.now(asia_time)
    time = country_time.strftime("%H:%M:%S")
    china_time = "Currently it is " + time + " in China"
    await message.channel.send(china_time)



  if any(word in message.content.lower() for word in ["china", "kina"]):
    with open('chinaNegative.txt') as c:
      lines3 = list(c.readlines())
      converted_list = []
      for element in lines3:
        converted_list.append(element.strip())

    if any(word in message.content.lower() for word in converted_list):
      member = message.author
      keywords = ["Ignorant", "Clueless", "Uneducated", "Uninformed"]
      await member.edit(nick=random.choice(keywords))

    else:
      if not message.author.bot:
       await message.channel.send("I heard someone talk about China, but was not able to detect anything negative.")

      if message.author == client.user:
        return



client.run(os.getenv('TOKEN'))
