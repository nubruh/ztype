import discord
import os
import requests
import json
from weather import *

api_key = "7bd306d17b6cfce742c53ec509c4cff2"
base_url = "http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}&units=metric"

client = discord.Client()

async def weather(city: str):
  city_name = city
  complete_url = base_url.replace('{API key}', api_key)
  complete_url = complete_url.replace('{city name}', city_name)
  response = requests.get(complete_url)
  json_data = json.loads(response.content)
  info = json_data
  return info




@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$w'):
    loc = message.content
    loc = loc.replace('$w' , '')
    w = await weather(loc)
    w = p_data(w)
    await message.channel.send(embed=w_message(w, loc))
    


client.run(os.getenv('TOKEN'))
