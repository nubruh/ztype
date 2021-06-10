import discord

color = 0xFF6500

key_features = {
    'temp' : 'Temperature',
    'feels_like' : 'Feels Like',
    'temp_min' : 'Minimum Temperature',
    'temp_max' : 'Maximum Temperature'
}

def p_data(data):
  data = data['main']
  del data['humidity']
  del data['pressure']
  return data

def w_message(data, location):
  location = location.title()
  message = discord.Embed(title=f'{location} weather', color = color ) 
  for key in data:
    message.add_field(
    name=key_features[key],
    value=str(data[key]),
    inline=False
    )
  return message 
