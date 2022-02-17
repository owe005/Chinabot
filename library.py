import discord #discord
import os
import pytz #chinatime
import random
import string
import requests, json
import time
import pandas as pd
from googletrans import Translator
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime #chinatime
from random import choice
from tabulate import tabulate
from discord_slash import SlashCommand, SlashContext
import re
import numpy as np
import matplotlib.pyplot as plt
import asyncpraw

from plotFunction import *

TOKEN = os.environ['TOKEN']


reddit = asyncpraw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')

api_key = ""
base_url = "http://api.openweathermap.org/data/2.5/weather?"

Users = []

userIndex = {
  'username':0
}

birthdays = {
  'name':"01/1",
}