from library import *

#vars
lizard_subreddit = reddit.subreddit("lizards")
dog_subreddit = reddit.subreddit("dogpictures")

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
  var = str(message.content)
  with open('socialCredit.txt',"r") as read:
      checkdata = read.readlines()
      wantedData = checkdata[0]
      wantedDataAsInt = int(checkdata[0])

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

  with open("positiveCount.txt","r") as po:
      data = po.readlines()
      count = int(data[0])

  if message.author == client.user:
    ##Low effort way to keep the bot nickname consistent by changing it back whenever someone sends a message and the bot replies.
    await message.author.edit(nick="Chinese Embassy")

  if message.author.bot == True:
    return

  if var == "based":
      await message.channel.send("based on what?")

  if message.content.lower().startswith(""):
    author = str(message.author)
    channel = str(message.channel)

    if channel == "grabrantstranark":
        return

    if channel == "chinese-translation":
        translator = Translator()
        results = translator.translate(var, dest='zh-cn')
        await message.channel.send(results.text)

    if channel == "english-translation":
        translator2 = Translator()
        results5 = translator2.translate(var, dest='en')
        await message.channel.send(results5.text)

    if author == "Magvy#0852":
        await message.add_reaction("🇨🇳")

    if wantedDataAsInt < 0:
        percentageBase = 0.10
        if random.random() < percentageBase:
            questionBank = ["China is the best country in the world, you will learn this soon", "This server has negative social credit and the Chinese government are getting impatient", "We see everything you do and say", "We know everything about you", "Have you learnt about Chinese culture today? We hope you have", "China > Every other country", "Nothing ever happened in Tiananmen Square"]
            pickRandomQuestion = random.choice(questionBank)
            await message.author.send(pickRandomQuestion)

  if message.content.startswith('c.lightshot'):
    channel4 = str(message.channel)
    randomurlString = string.ascii_lowercase + string.digits
    randomizing = ''.join(random.choice(randomurlString) for i in range(6))
    url = "https://prnt.sc/" + str(randomizing)
    await message.channel.send(url)

  if message.content.startswith('c.about'):
        embedVar = discord.Embed(title="Who am I?", description="I am a representative of the People's Republic of China acting on the interests of the greatest country on Earth. I am here to make sure the server keeps it's social credit positive.\n\nIf not I will start taking action against people.", color=0xff0000)
        embedVar.add_field(name="Available Commands", value = "These are the available commands that the People's Republic of China has allowed me to reveal: \n \n translations in #chinese-translation and #english-translation \n\nPrefix = c.\n e.g: c.about \n\n about \n flipcoin \n socialcredits \n lightshot \n chinatime \n funfact \n \n", inline=False)
        embedVar.set_footer(text="All non-citizens of China are subject to voluntarily labour within our labour-camps within due date. \n \nAuthor: Ole Westby")
        embedVar.set_thumbnail(url="https://cdn.pixabay.com/photo/2020/04/04/11/45/flag-5001937_960_720.jpg")
        await message.channel.send(embed=embedVar)

  if message.content.startswith("c.funfact"):
    with open('facts.txt') as f:
      lines = f.readlines()
      random_int = random.randint(0,len(lines)-1)
      randomFact = lines[random_int]
    await message.channel.send(randomFact)

  if message.content.startswith("c.socialcredits"):
    responding = "This server has " + wantedData + " social credits available to spend."
    await message.channel.send(responding)

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


  ### Commence animal pictures ###

  if any(word in message.content.lower() for word in ["lizard", "øgle"]):
      all_subs_liz = []
      top_liz = lizard_subreddit.hot(limit=50)
      for submission in top_liz:
          all_subs_liz.append(submission)
      random_sub_liz = random.choice(all_subs_liz)
      name_liz = random_sub_liz.title
      url_liz = random_sub_liz.url
      em_liz = discord.Embed(title=name_liz)
      em_liz.set_image(url=url_liz)
      await message.channel.send(embed=em_liz)

  if any(word in message.content.lower() for word in ["dog", "hund"]):
      all_subs_dog = []
      top_dog = dog_subreddit.hot(limit=50)
      for submission in top_dog:
          all_subs_dog.append(submission)
      random_sub_dog = random.choice(all_subs_dog)
      name_dog = random_sub_dog.title
      url_dog = random_sub_dog.url
      em_dog = discord.Embed(title=name_dog)
      em_dog.set_image(url=url_dog)
      await message.channel.send(embed=em_dog)

  ###

  if any(word in message.content.lower() for word in ["china", "kina"]):
    if any(word in message.content.lower() for word in converted_list + converted_list_2) == True:
      wantedDataAsInt += -5000
      data[0] = str(wantedDataAsInt)

      with open("socialCredit.txt","w") as neg:
          neg.writelines(data)
          neg.close()

      await message.add_reaction("❓")
      await message.add_reaction("🤔")
      await message.add_reaction("❔")

      indRep = ("You have either said a postive thing and a negative thing, or you are messing with us. That's still -5000 points. " + str(wantedDataAsInt) + " is the new social credit score (-5000)")
      await message.channel.send(indRep)


    elif any(word in message.content.lower() for word in converted_list):
      member = message.author
      keywords = ["Ignorant", "Clueless", "Uneducated", "Uninformed"]
      wantedDataAsInt += -5000
      data[0] = str(wantedDataAsInt)

      with open("socialCredit.txt","w") as neg:
          neg.writelines(data)
          neg.close()

      await message.add_reaction("👎")
      await message.add_reaction("😠")
      await message.add_reaction("🤥")

      response2 = ("You have no idea what you are talking about. You have earned a new name for yourself, dog. \nThis server's available social credit has now hit: " + str(wantedDataAsInt) + "... a decrease of 5000 points 😠")
      await message.channel.send(response2)

      await member.edit(nick=random.choice(keywords))

    elif any(word in message.content.lower() for word in converted_list_2):
      wantedDataAsInt += 1000
      data[0] = str(wantedDataAsInt)

      with open("socialCredit.txt","w") as pos:
        pos.writelines(data)
        pos.close()

      await message.add_reaction("👍")
      await message.add_reaction("🇨🇳")
      await message.add_reaction("👏")

      response = ("I detected a positive thing said about China! \nThis server's available social credit has now hit: " + str(wantedDataAsInt) + "... an increase of 1000 points 🤩")
      await message.channel.send(response)

    else:
      if 'c.chinatime' in message.content:
        return

      else:
        await message.channel.send("I heard someone talk about China, but was not able to detect anything negative.")

client.run(TOKEN)
