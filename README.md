# KarmaWhore

Reposts old shit from the past for useless internet points. Using it, I was able to get just over 100,000 karma in under 72 hours.

## Setup

You'll need a Linux distro. Any distro that supports Python, Nano, Pip3 and Git will work. It might work on Windows/Mac, but I haven't tested that out.

Download the bot, change into its directory:

    git clone https://github.com/IThinkImOKAY/KarmaBot && cd KarmaBot

Install the needed packages:

    pip3 install -r requirements.txt

### Getting API Keys

#### Imgur

- Go to [/oauth2/addclient](https://api.imgur.com/oauth2/addclient)
- Fill in the form and get your Imgur client ID.


#### Reddit

- Go to [/prefs/apps](https://old.reddit.com/prefs/apps)
- Select "are you a developer? create an app..."
- Name it whatever you want to, but select "script"
- Fill in the rest of the form

Edit the configuration file:

    nano config.yaml

- Edit "c_id" with the "personal use script"
- Edit "c_s" with the secret
- Edit "u_a" with the bot's description
- Edit "i_id" with your Imgur client id
- For the list of subs, add some subs that you wish to repost from
- Save the file (ctrl x and Y)

## Run the bot:

    python3 main.py
