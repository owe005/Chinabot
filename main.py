import discord
import os
import pytz
import random
import emoji
import string
from googletrans import Translator
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime
from random import choice

client = discord.Client()

status = cycle(["Surveillance Simulator", "Assassinating Defectors 2", "Hearts of Iron IV as Xi Jinping"])

@client.event
async def on_ready():
  change_status.start()
  print("China Embassy is online and ready")

@tasks.loop(seconds=300)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_message(message):

  if message.author == client.user:
    return

  if message.author.bot == True:
    return

  if message.content.lower().startswith(""):
    channelCheck = str(message.channel.id)
    if channelCheck == "745725475157967000":
        return

    channel = str(message.channel)
    if channel == "chinese-translation":
      with open("socialCredit.txt","r") as check:
        data3 = check.readlines()
        creditCount2 = int(data3[0])

        if creditCount2<0:
            await message.channel.send("Not enough social credit to ask for a translation")

        if creditCount2>=0:
            translator = Translator()
            input_text = str(message.content)
            results = translator.translate(input_text, dest='zh-cn')
            creditCount2 += -100
            data3[0] = str(creditCount2)

            with open("socialCredit.txt","w") as change:
                change.writelines(data3)
                change.close()

            finalized = ("This translation costed the server 100 social credits, server now has " + str(creditCount2) + " credits. \nYour message was translated into:\n" + results.text)

            await message.channel.send(finalized)

    TheUser = str(message.author)
    if TheUser == "Magvy#0852":
        await message.add_reaction("🇨🇳")

    with open("socialCredit.txt","r") as check2:
        data4 = check2.readlines()
        socialCreditCount = int(data4[0])
        if socialCreditCount < 0:
            percentageBase = 0.10
            if random.random() < percentageBase:
                questionBank = ["China is the best country in the world, you will learn this soon", "This server has negative social credit and the Chinese government are getting impatient", "We see everything you do and say", "We know everything about you", "Have you learnt about Chinese culture today? We hope you have", "China > Every other country", "Nothing ever happened in Tiananmen Square"]
                pickRandomQuestion = random.choice(questionBank)
                await message.author.send(pickRandomQuestion)

  if message.content.startswith('c.cities'):
      cities = ["beijing.jpeg", "shanghai.jpg", "idk.jpg", "idk2.jpg"]
      pickRandomCity = random.choice(cities)
      await message.channel.send(file=discord.File(pickRandomCity))

  if message.content.startswith('c.lightshot'):
      randomurlString = string.ascii_lowercase + string.digits
      randomizing = ''.join(random.choice(randomurlString) for i in range(6))
      url = "https://prnt.sc/" + str(randomizing)
      await message.channel.send(url)

  if message.content.startswith('c.about'):
        embedVar = discord.Embed(title="Who am I?", description="I am a representative of the People's Republic of China acting on the interests of the greatest country on Earth. I am here to make sure the server keeps it's social credit positive.\n\nIf not I will start taking action against people.", color=0xff0000)
        embedVar.add_field(name="Available Commands", value = "These are the available commands that the People's Republic of China has allowed me to reveal: \n \n translations in #chinese-translation \n\nPrefix = c.\n e.g: c.about \n\n about \n cities \n flipcoin \n socialcredits \n lightshot \n chinatime \n hongkongtime \n realfact \n funfact \n \n", inline=False)
        embedVar.set_footer(text="All non-citizens of China are subject to voluntarily labour within our labour-camps within due date. \n \nAuthor: Ole Westby")
        embedVar.set_thumbnail(url="https://cdn.pixabay.com/photo/2020/04/04/11/45/flag-5001937_960_720.jpg")
        await message.channel.send(embed=embedVar)

  if message.content.startswith("c.funfact"):
    with open('facts.txt') as f:
      lines = f.readlines()
      random_int = random.randint(0,len(lines)-1)
      randomFact = lines[random_int]
    await message.channel.send(randomFact)

  if message.content.startswith("c.realfact"):
    with open('importantFacts.txt') as s:
      lines2 = s.readlines()
      random_int_2 = random.randint(0, len(lines2)-1)
      realFact = lines2[random_int_2]
    await message.channel.send(realFact)

  if message.content.startswith("c.socialcredits"):
    with open('socialCredit.txt') as ss:
      checkdata = ss.readlines()
      wantedData = checkdata[0]
    responding = "This server has " + wantedData + " social credits available to spend."
    await message.channel.send(responding)

  if message.content.lower().startswith(""):
      var = str(message.content)
      if var == "based":
          await message.channel.send("based on what?")

  if 'based on what' in message.content:
    await message.channel.send("your mom")

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



  if 'your mom' in message.content:
    await message.channel.send("你会死")



  if message.content.startswith('c.chinatime'):
    asia_time = pytz.timezone('Asia/Shanghai')
    country_time = datetime.now(asia_time)
    time = country_time.strftime("%H:%M:%S")
    china_time = "Currently it is " + time + " in China"
    await message.channel.send(china_time)

  if message.content.startswith('c.hongkongtime'):
    hk_time = pytz.timezone('Asia/Shanghai')
    country2_time = datetime.now(hk_time)
    time2 = country2_time.strftime("%H:%M:%S")
    hk_time2 = "Currently it is " + time2 + " in China"
    await message.channel.send(hk_time2)

  if any(word in message.content.lower() for word in ["china", "kina"]):
    with open('chinaNegative.txt') as n:
      lines3 = list(n.readlines())
      converted_list = []
      for element in lines3:
        converted_list.append(element.strip())

    with open('chinaPositive.txt') as p:
      lines4 = list(p.readlines())
      converted_list_2 = []
      for element in lines4:
        converted_list_2.append(element.strip())

    if any(word in message.content.lower() for word in converted_list):
      member = message.author
      keywords = ["Ignorant", "Clueless", "Uneducated", "Uninformed"]
      with open("socialCredit.txt","r") as ne:
        data2 = ne.readlines()
        creditCount = int(data2[0])
        creditCount += -5000
        data2[0] = str(creditCount)

      with open("socialCredit.txt","w") as neg:
          neg.writelines(data2)
          neg.close()
      socialCredit = str(data2[0])
      await message.add_reaction("👎")
      await message.add_reaction("😠")
      await message.add_reaction("🤥")
      response2 = ("You have no idea what you are talking about. You have earned a new name for yourself, dog. \nThis server's available social credit has now hit: " + socialCredit + "... a decrease of 5000 points 😠")
      await message.channel.send(response2)
      await member.edit(nick=random.choice(keywords))

    elif any(word in message.content.lower() for word in converted_list_2):
      with open("positiveCount.txt","r") as po:
        data = po.readlines()
        count = int(data[0])
        count += 1
        data[0] = str(count)

      with open("positiveCount.txt","w") as pos:
        pos.writelines(data)
        pos.close()

      pCount = str(data[0])

      with open("socialCredit.txt","r") as posi:
        data2 = posi.readlines()
        creditCount = int(data2[0])
        creditCount += 1000
        data2[0] = str(creditCount)

      with open("socialCredit.txt","w") as posit:
        posit.writelines(data2)
        posit.close()

      socialCredit = str(data2[0])

      response = ("I detected a positive thing said about China, " + pCount + " positive things have been said about China so far in this server! \nThis server's available social credit has now hit: " + socialCredit + "... an increase of 1000 points 🤩")
      emoji = '\N{THUMBS UP SIGN}'
      await message.add_reaction(emoji)
      await message.add_reaction("🇨🇳")
      await message.add_reaction("👏")
      await message.channel.send(response)

    else:
      if 'c.chinatime' in message.content:
        return

      else:
        await message.channel.send("I heard someone talk about China, but was not able to detect anything negative.")

client.run('NzQ4NTQ1MTI0NjYwNjc0Njky.X0e--Q.R5FW7K2mqnGZQ9zY1SJOxtYIuZw')
