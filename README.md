# KarmaBot

![](award.png)

Reposts old shit from the past for useless internet points. I was able to get just over 100,000 karma in under 72 hours.

## Set-up

Download the bot, change into the directory:

    git clone https://github.com/IThinkImOKAY/KarmaBot && cd KarmaBot

Install the needed packages:

    pip3 install praw pyyaml pyimgur

Getting API Keys

- You can get your Imgur credentials from [here](https://api.imgur.com/oauth2/addclient)
- Follow [James Briggs' uide](https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c) to get your reddit API keys

Edit the YAML file:


- `client_id` is your reddit client ID
- `client_secret` is your reddit client secret
- `user_agent` should be a short description about your bot
- `username` is your reddit username
- `password` is your reddit password
- `imgur_id` is your imgur client id

I recommend using cron to schedule the bot to run to your liking :)
