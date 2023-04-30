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
 
  ### How To Get A Custom Steam URL
  - Login to Steam's website.
  - Click on your display name in the top-right of the screen and then select View Profile from the dropdown menu.
  - On the right-hand side of the screen, click Edit Profile.
  - In the Custom URL field, type out your custom URL.
  - Scroll down to the bottom of the page and click Save.
 
 Example: https://steamcommunity.com/id/yoursteamid
 
