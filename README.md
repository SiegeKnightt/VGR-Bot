# VGR-Bot
This Discord bot will compare two player's steam libraries and then lists the games they have in common and then provides a suggestion for a game they should play together.
This bot utilizes the Discord API and Steam API.
The goal of this project was to better understand how to implement API's and create a way for my friends and I to easily see which games we all own.

## Deployment Instructions
 - Create a .env file with your discord key, discord server name, and Steam API key
 - Change line 51 to contain your channel ID
 - Run the bot with py bot.py
 - Use !compare steam_id_1 steam_id_2
 
 NOTE: To find your steam id, go to your steam profile and look at the link. You must have a custom URL set for this to work.
 
 Example: https://steamcommunity.com/id/yoursteamid
 
 https://www.makeuseof.com/how-to-set-up-custom-url-steam-profile/#:~:text=Head%20to%20the%20Steam%20website,type%20out%20your%20desired%20URL.
