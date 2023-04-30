"""
VGR Bot (Video Game Recommendation Bot)
Author: Reeves Farrell

Description:
- Discord bot to give a random video game recommendation based on two users steam libraries
- Utilizes the Discord API and Steam API
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
STEAM_API_TOKEN = os.getenv('STEAM_API_TOKEN')

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
    channel = bot.get_channel(yourchannelnumberhere)
    await channel.send(f'Hi {member.name}, use !assist for commands and !compare for a random game recommendation!')

# Command for telling users how to use the bot when joining
@bot.command()
async def assist(ctx):
    await ctx.channel.send(f'Use !compare steam_id_1 steam_id_2 to compare games!')

# Command to compare steam libraries
# !compare steam_id_1 steam_id_2
@bot.command()
async def compare(ctx, profile_name_1, profile_name_2):
    # Steam API endpoint for retrieving Steam ID from profile name
    url = f"https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={STEAM_API_TOKEN}&vanityurl={profile_name_1}"
    url_2 = f"https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={STEAM_API_TOKEN}&vanityurl={profile_name_2}"

    # Sends GET requests to Steam API to retrieve Steam ID for each profile name
    response_1 = requests.get(url)
    response_2 = requests.get(url_2)

    # Checks if requests were successful
    if response_1.status_code != 200:
        await ctx.send("Error: Failed to retrieve Steam IDs for user one.")
        return
    elif response_2.status_code != 200:
        await ctx.send("Error: Failed to retrieve Steam IDs for user two.")
        return

    # Parses response JSON to retrieve Steam ID for each profile name
    steam_id_1 = response_1.json().get("response", {}).get("steamid")
    steam_id_2 = response_2.json().get("response", {}).get("steamid")

    # Steam API endpoint for retrieving list of games in a user's library
    url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={STEAM_API_TOKEN}&steamid={steam_id_1}&include_appinfo=1&include_played_free_games=1&format=json"
    url_2 = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={STEAM_API_TOKEN}&steamid={steam_id_2}&include_appinfo=1&include_played_free_games=1&format=json"

    # Sends GET requests to Steam API to retrieve list of games for each user
    response_1 = requests.get(url)
    response_2 = requests.get(url_2)

    # Checks if requests were successful
    if response_1.status_code != 200:
        await ctx.send("Error: Failed to retrieve game libraries for user one.")
        return
    elif response_2.status_code != 200:
        await ctx.send("Error: Failed to retrieve game libraries for user two.")
        return

    # Parses response JSON to retrieve list of games for each user
    games_1 = response_1.json().get("response", {}).get("games", [])
    games_2 = response_2.json().get("response", {}).get("games", [])

    # Finds common games in both users' libraries
    common_games = set([game["name"] for game in games_1]) & set([game["name"] for game in games_2])

    # Checks if there are any common games
    if len(common_games) == 0:
        await ctx.send("There are no common games in the libraries of these two users.")
        return

    # Selects a random game from the list of common games
    random_game = random.choice(list(common_games))

    # Converts the set of common games to a string for display
    common_games_str = "\n".join(common_games)

    # Sends the list of common games as a message to the channel
    await ctx.send("Common games:\n" + common_games_str)

    # Sends the random game as a message to the channel
    await ctx.send(f"You guys should play {random_game}!")

bot.run(TOKEN)
