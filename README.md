# VGR-Bot
This is a Discord bot that gives a random video game recommendation by using the Discord API and Steam API.
The goal of this project was to better understand how to implement API's and create a fun game suggester for my friends and I.
The bot will compare two player's steam libraries and then lists the games they have in common and then provides a suggestion for a game they should play together.

## Deployment Instructions
 - Create a .env file with your discord key, discord server name, and Steam API key
 - Change line 51 to contain your channel ID
 - Run the bot with py bot.py
 - Use !compare steam_id_1 steam_id_2
 NOTE: To find your steam id, go to your steam profile and look at the link
 Example: https://steamcommunity.com/id/yoursteamid
