from library import *

#vars
lizard_subreddit = reddit.subreddit("FiftyFifty")
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

  with open("susCount.txt","r") as sus:
      data = sus.readlines()
      susCount = data[0]
      susCountAsInt = int(data[0])

  if message.author == client.user:
    ##Low effort way to keep the bot nickname consistent by changing it back whenever someone sends a message and the bot replies.
    await message.author.edit(nick="Chinese Embassy")

  if message.author.bot == True:
    return

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

  if message.content.startswith('c.lightshot'):
    channel4 = str(message.channel)
    randomurlString = string.ascii_lowercase + string.digits
    randomizing = ''.join(random.choice(randomurlString) for i in range(6))
    url = "https://prnt.sc/" + str(randomizing)
    await message.channel.send(url)


  if message.content.startswith('c.price '):
    x_binance =  pd.DataFrame(Bclient.get_ticker())
    x_binance = x_binance[x_binance.symbol.str.contains("USDT")]
    x_binance = x_binance[~(x_binance.symbol.str.contains("UP") | x_binance.symbol.str.contains("DOWN"))]

    ticker = str(message.content[8:])
    ticker = ticker.upper()
    x_binance = x_binance[x_binance.symbol.str.contains(ticker)]
    x_binance = x_binance[["symbol", "lastPrice"]]
    x_binance = x_binance.to_string(header=False)
    await message.channel.send(x_binance)

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

  if message.content.startswith('c.gay'):
      percentageBase = random.randint(1,100)
      percentageBaseAsPercentage = str(percentageBase) + "%"
      response = "You are " + str(percentageBaseAsPercentage) + " gay"
      await message.channel.send(response)

  if message.content.startswith('c.lol'):
      randomChamp = random.choice(allchamp)
      response = "You should play as " + str(randomChamp)
      await message.channel.send(response)

  if message.content.startswith('c.function '):
      msg = int((message.content[11:]))
      x = np.linspace(-5,5,100)
      y = x**msg
      plt.plot(x,y)
      plt.legend(["x^"+str(msg)])

      figure = "figures/figure"+str(random.sample(range(100000), 1)) +".jpg"
      plt.savefig(figure)
      plt.close()
      await message.channel.send(file=discord.File(figure))

  if message.content.startswith('c.about'):
        embedVar = discord.Embed(title="Who am I?", description="I am a representative of the People's Republic of China acting on the interests of the greatest country on Earth.", color=0xff0000)
        embedVar.add_field(name="Available Commands", value = "These are the available commands that the People's Republic of China has allowed me to reveal: \n \n translations in #chinese-translation and #english-translation \n\nPrefix = c.\n e.g: c.about \n\n about \n flipcoin \n gay \n price \n lol \n lightshot \n chinatime \n funfact \n \n", inline=False)
        embedVar.set_footer(text="All non-citizens of China are subject to voluntarily labour within our labour-camps within due date. \n \nAuthor: Ole Westby")
        embedVar.set_thumbnail(url="https://cdn.pixabay.com/photo/2020/04/04/11/45/flag-5001937_960_720.jpg")
        await message.channel.send(embed=embedVar)

  if message.content.startswith("c.funfact"):
    with open('facts.txt') as f:
      lines = f.readlines()
      random_int = random.randint(0,len(lines)-1)
      randomFact = lines[random_int]
    await message.channel.send(randomFact)

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

  if any(word in message.content.lower() for word in ["sus"]):
      susCountAsInt+=1
      data[0] = str(susCountAsInt)

      with open("susCount.txt","w") as susFin:
          susFin.writelines(data)

      await message.channel.send(file=discord.File("sus.jpg"))
      desOut = ("'sus' has been said "+data[0]+" time(s)")
      await message.channel.send(desOut)


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
client.run(TOKEN)
