# Karma Bot
**Reposts old shit from the past for useless internet points!!!**

# Getting set up
**This guide should help you get the bot running**

* Figure out how to install Python
* Figure out how to install Pip
* Install Git
* Run the following in your terminal

        git clone https://github.com/Mr-Steal-Your-Script/KarmaBot
        cd KarmaBot/old
        pip3 install -r requirements.txt

* Create a reddit app
    * Go to [/prefs/apps](https://www.reddit.com/prefs/apps/)
    * Select "are you a developer? create an app..."
    * Name it whatever you want to
    * Select "script"
    * For the description, leave a short description about the bot
    * Leave "about url" blank
    * For the "redirect uri", put a link to your favorite porno
* Create an imgur app
    * Go to [/oauth2/addclient](https://api.imgur.com/oauth2/addclient)
    * Name it whatever
    * For the "Authorization callback URL:", put a link to your favorite porno
    * Fill in your email address
    * Leave a short description about the bot
    * Prove that you aren't a robot    
* Open [config.py](https://github.com/Mr-Steal-Your-Script/LegitKarmaBot/blob/master/config.py) in your favorite text editor
    * Edit "C_ID" with the "personal use script"
    * Edit "C_S" with the secret
    * Edit "U_A" with the bot's description
    * Edit "UN" with the bot's username
    * Edit "PW" with your bot's password
    * Edit "I_ID" with your imgur client id
* In your terminal run the following:

      python3 main.py
