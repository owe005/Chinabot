##################################################################################
###                           CHINABOT Version 1.0.0                           ###
##################################################################################
### Disclaimer: This is just for jokes, nothing is meant to be taken seriously ###
##################################################################################
###                               Author: @owe005
##################################################################################

from library import * ### Bad practice, but implemented for simplicity

client = discord.Client()
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.
guild_ids = [] # Put your server id here.

@slash.slash(name="help", description="Documentation", guild_ids=guild_ids)
async def _help(ctx):

  embed=discord.Embed(title="Page 1/2\n\nChinese Embassy -  Documentation", description="These are the available commands and features that the People's Republic of China has allowed me to reveal.", color=0xff0000)
  embed.set_author(name="Github", url="https://github.com/owe005/Chinabot", icon_url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
  embed.add_field(name="/chinatime", value="The reason why this bot was created in the first place. This command will return the current time in mainland China.", inline=False)
  embed.add_field(name="/flipacoin", value="This command will simply flip a coin for you and display it in an embedded message for you to view.", inline=False)
  embed.add_field(name="/lightshot", value="Will generate a random URL from prnt.sc/ for you to view. There is a chance that the image might be deleted, if that is the case, just try again! For the x10 version, it returns 10 generated image links.", inline=False)
  embed.add_field(name="/ssl", value="This is game of Stein Saks Laks! The rules of this game are:\nStein beats Saks and Laks.\nSaks beats Laks but loses to Stein.\nLaks loses to Stein and Laks.\nIf both pick the same, it's a tie.\nWill you risk playing Saks?", inline=False)
  embed.set_footer(text="This bot is a satirical parody of the Chinese government - don't take it seriously.")

  embed2=discord.Embed(title="Page 2/2\n\nChinese Embassy -  Documentation ", description="These are the available commands and features that the People's Republic of China has allowed me to reveal. ", color=0xff0000)
  embed2.set_author(name="Github", url="https://github.com/owe005/Chinabot", icon_url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
  embed2.add_field(name="/plot {function}", value="The plot command is probably the most useful command added to this god forsaken bot. To put it simply, run /plot followed by the function you wish to plot. For example: /plot x^3+sin(2*x)-(5/x)+ln(x) That's it! It is important to separate x variables with a * or else it will not run. E.g 2*x and not 2x.", inline=False)
  embed2.add_field(name="/reddit {subreddit}", value="This command will return a random image from a subreddit of your choosing.", inline=False)
  embed2.add_field(name="/weather {city}", value="As obvious as this is, I'll still explain it. You run /weather and give it a city name. For example /weather bergen.", inline=False)
  embed2.set_footer(text="This bot is a satirical parody of the Chinese government - don't take it seriously. ")

  message = await ctx.send(embed = embed)
  def check(reaction, user):
    return user == ctx.author

  await message.add_reaction('◀')
  await message.add_reaction('▶')

  i = 0
  reaction = None
  pages = [embed,embed2]

  while True:
    if str(reaction) == '◀':
      if i > 0:
        i -= 1
        await message.edit(embed = pages[i])

    elif str(reaction) == '▶':
      if i < 2:
        i += 1
        await message.edit(embed = pages[i])

    try:
      reaction, user = await client.wait_for('reaction_add', timeout = 30.0, check = check)
      await message.remove_reaction(reaction, user)

    except:
      break

  await message.clear_reactions()

@slash.slash(name="ssl", description="STEIN, SAKS, LAKS!", guild_ids=guild_ids)
async def _rps(ctx, choice: str):
  choices=["stein", "saks", "laks"]
  if choice.lower() not in choices:
    await ctx.send("Error: Stein, saks eller laks?")
  else:
    bot_choice = random.choice(choices)

    if (choice.lower() == bot_choice.lower()):
      embed = discord.Embed(title=f"Vi begge valgte {choice}. Uavgjort!")
      await ctx.send(embed=embed)

    elif (choice.lower() == "stein"):
      if (bot_choice.lower() == "saks"):
        embed = discord.Embed(title="Du valgte stein, jeg valgte saks. You win.")
        await ctx.send(embed=embed)

      else:
        embed = discord.Embed(title="Du valgte stein, jeg valgte laks. I cannot win, therefore you win.")
        await ctx.send(embed=embed)

    elif (choice.lower() == "saks"):
      if (bot_choice.lower() == "stein"):
        embed = discord.Embed(title="Du valgte saks, jeg valgte stein. I win.")
        await ctx.send(embed=embed)

      else:
        embed = discord.Embed(title="Du valgte saks, jeg valgte laks. I cannot win, therefore you win.")
        await ctx.send(embed=embed)

    elif (choice.lower() == "laks"):
      if (bot_choice.lower() == "stein"):
        embed = discord.Embed(title="Du valgte laks, jeg valgte stein. You cannot win, therefore I win.")
        await ctx.send(embed=embed)

      else:
        embed = discord.Embed(title="Du valgte laks, jeg valgte saks. You cannot win, therefore I win.")
        await ctx.send(embed=embed)

@slash.slash(name="lightshot", description="Generate random Lightshot URL", guild_ids=guild_ids)
async def _lightshot(ctx): 
      randomurlString = string.ascii_lowercase + string.digits
      randomizing = ''.join(random.choice(randomurlString) for i in range(6))
      url = "https://prnt.sc/" + str(randomizing)
      await ctx.send(url)

@slash.slash(name="flipacoin", description="Flip a coin!", guild_ids=guild_ids)
async def _flipacoin(ctx): 
      deter = [1, 0]
      if random.choice(deter) == 1:
          embedVar2 = discord.Embed(title="Heads!", description="You rolled heads bro", color=0xff0000)
          embedVar2.set_thumbnail(url="https://www.pngkey.com/png/full/146-1464786_400px-circle-quarter-heads-side-of-coin.png")
          await ctx.send(embed=embedVar2)
      else:
          embedVar3 = discord.Embed(title="Tails!", description="You rolled tails bro", color=0xff0000)
          embedVar3.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
          await ctx.send(embed=embedVar3)

@slash.slash(name="chinatime", description="Returns current time in China", guild_ids=guild_ids)
async def _chinatime(ctx): 
      asia_time = pytz.timezone('Asia/Shanghai')
      country_time = datetime.now(asia_time)
      time = country_time.strftime("%H:%M:%S")
      china_time = f"Currently it is {time} in China"
      embedMsg = discord.Embed(title=china_time)
      await ctx.send(embed=embedMsg)

@slash.slash(name="weather", description="Give a city name and it will return the current weather", guild_ids=guild_ids)
async def _weather(ctx, city: str):
      city_name = str(city)
      complete_url = base_url + "appid=" + api_key + "&q=" + city_name
      response = requests.get(complete_url)
      x = response.json()

      if x["cod"] != "404": # If it does not return 404.
          y = x["main"]
          current_temperature = y["temp"]
          current_temperature = current_temperature - 273.15
          current_temperature = round(current_temperature, 2)
          z = x["weather"]
          weather_description = z[0]["description"]
          embedWeather = discord.Embed(title=f"Information about {city_name.capitalize()}", description=f"The current temperature is {current_temperature} ℃ with {weather_description}", color=0xff0000)
          await ctx.send(embed=embedWeather)

      else:
          await ctx.send("Place not found") # Else, it returned 404

@slash.slash(name="plot", description="Take adventage of matplotlib from China!", guild_ids=guild_ids)
async def _plot(ctx, function: str):
    x = np.linspace(-5,5,100)
    y = string2func(function)
    plt.plot(x,y(x))
    plt.legend([function])
    figure = "figures/figure"+str(random.sample(range(100000), 1)) +".jpg"
    plt.savefig(figure)
    plt.close()
    await ctx.send(file=discord.File(figure))
    os.remove(figure)

@slash.slash(name="reddit", description="Return image from subreddit", guild_ids=guild_ids)
async def _reddit(ctx, sub: str):
  subreddit = await reddit.subreddit(sub)
  all_subs = []
  top = subreddit.hot(limit=50)
  async for submission in top:
    all_subs.append(submission)

  random_sub = random.choice(all_subs)
  name = random_sub.title
  url = random_sub.url
  em = discord.Embed(title=name)
  em.set_image(url=url)
  em.set_footer(text="If it does not load, try again. It is because of posts linking to imgur,gyazo, etc..")
  await ctx.send(embed=em)

@client.event
async def on_ready(): #O(1)
  change_status.start()
  clownOfMonth.start()
  happyBirthday.start()
  print("Chinese Embassy is online and ready")

### Status Change
@tasks.loop(hours=1) # Runs every 5 min.
async def change_status():
  status = cycle(["Surveillance Simulator", "Assassinating Defectors 2", "Hearts of Iron IV as Xi Jinping"])
  await client.change_presence(activity=discord.Game(next(status)))
### End Status Change

### Clown of the Month
@tasks.loop(hours=24) # Runs every 24hrs.
async def clownOfMonth():
  channel = client.get_channel() # Insert channel to send message in.

  if (str(datetime.today().strftime('%d')) != "01"): # If not 01 of the current month, print status update.
    print("It is not the first of a given month.")

  elif (str(datetime.today().strftime('%d')) == "01"): # If it is, select random clown and send it in embedded message.

    channel = client.get_channel(745726336311623740)
    random_user = random.choice(Users)

    clownMsg = (f"Listen up everyone, {random_user} has been automatically chosen as the Clown of {datetime.today().strftime('%B')}\n\nThis action was done automatically, and may not be reverted.")
    
    embedMsg = discord.Embed(title=f"NEW Clown of the Month: {random_user}!",description=clownMsg, color=0xff0000)

    embedMsg.set_thumbnail(url="https://i.pinimg.com/originals/83/0d/56/830d5660e972a155a4e7b2c51240644b.jpg")

    await channel.send(embed=embedMsg)
### End Clown of the Month

### Happy Birthday Impl
@tasks.loop(hours=24) # Check everyday.
async def happyBirthday():
  channel = client.get_channel() # Insert channel to send message in.
  timezone = pytz.timezone("Europe/Amsterdam")
  day = str(datetime.now(timezone).day)
  month = str(datetime.now(timezone).month)
  dateNow = str(f"{day}/{month}")

  for i in birthdays:
    targetBday = str(birthdays[i])
    if dateNow == targetBday:
      output = f"@everyone - Happy Birthday to / Gratulerer med dagen til @{i}"

      print(f"It IS {i}'s birthday today")

      await channel.send(output)
### End Happy Birthday Impl

@client.event
async def on_message(message):
  var = str(message.content) # Save the message as a String.
  channel = str(message.channel) # Save the channel as a String
  
  if message.author.bot == True: ##Ignore Bots.
    return

  for i in var.split(): 
    if words_re.search(i): 
      with open("slurs.txt","r") as slur:
        slurs = slur.readlines()[0]
        slursToInt = int(slurs)
        slursToInt+=1
        slurString = str(slursToInt)

        with open("slurs.txt","w") as slurUpd:
          slurUpd.writelines(slurString)


  with open("chance.txt","r") as perc:
    prob = int(perc.readlines()[0])

    if random.randint(1,prob) == 1: 
    
      embedVar = discord.Embed(title=(f"HA U LOOKED!!!"), description=f"Congratulations, the odds of you receiving this message was 1 / {prob}! The odds have now been reset to 8192, but you don't have to tell them! :)", color=0xff0000)
      embedVar.set_image(url="https://cdn.discordapp.com/attachments/745725475157967000/942926568475463690/nooocat.jpg")

      probDec = str(8192)

      with open("chance.txt","w") as percUpd:
        percUpd.writelines(probDec)
        
      await message.author.send(embed = embedVar)

    else:
      prob-=1
      probInc = str(prob)

      with open("chance.txt","w") as percUpd:
        percUpd.writelines(probInc)


### Translations ### 

# Replace empty string with name of channel where you wish to have translations happen.

  if channel == "":
      translator = Translator()
      results = translator.translate(var, dest='zh-cn')
      await message.channel.send(results.text)

### End Translations ###


### Run Bot
client.run(TOKEN)
