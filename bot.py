"""
VGR Bot (Video Game Recommendation Bot)
Author: Reeves Farrell

Description:
- Discord bot to give a random video game recommendation
- Utilizes the Discord API and RAWG.io database API
- Goal was to better understand API's
"""

import os
import discord
import random
import requests

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Environment tokens
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
RAWG_API_TOKEN = os.getenv('RAWG_API_TOKEN')

# Gets intents for messages and member access
intents = discord.Intents.default()
intents.members = True
intents.message_content =  True

# Object representing the bot itself
bot = commands.Bot(command_prefix = '!', intents = intents)

# Function for giving bot info and server info to console
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name = GUILD)

    print('Logged in as {0.user}\n'.format(bot))

    print(f'{bot.user} has connected to the following server:')
    print(f'{guild.name}(id: {guild.id})\n')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Server Members:\n - {members}')

# Function for when someone joins the server
@bot.event
async def on_member_join(member):
    # Change ID to whatever channel is the welcome channel
    channel = bot.get_channel(1101910949235007521)
    await channel.send(f'Hi {member.name}, use !assist for commands and !game for a random game recommendation!')

# Command for telling users how to use the bot when joining
@bot.command()
async def assist(ctx):
    await ctx.channel.send(f'Use !game for a random game recommendation!')

# Command to give a random game recommendation
# Uses the RAWG.io API to gather the game data
@bot.command(name='game')
async def game(ctx):
    headers = {
        'User-Agent': 'Discord Bot'
    }

    params = {
        'key': RAWG_API_TOKEN,
        'page_size': 100,
        'sort-by': 'rating',
        'platforms': '18,1'
    }

    response = requests.get('https://api.rawg.io/api/games', headers = headers, params = params).json()

    game_list = response['results']

    game = random.choice(game_list)

    platforms = game['platforms']

    # Creates list of platforms with their corresponding ids
    platform_numbers = [platform['platform']['id'] for platform in platforms]

    # Chooses a random avaliable platform
    random_platform_number = random.choice(platform_numbers)

    # Finds a match with the platform and the game
    platform_name = next((platform['platform']['name'] for platform in platforms if platform['platform']['id'] == random_platform_number), None)

    # Prints the game and platform or states a platform was not found
    if platform_name:
        await ctx.send(f'You should try playing {game["name"]} on {platform_name}.')
    else:
        await ctx.send(f'Could not find a platform for {game["name"]}.')

bot.run(TOKEN)
