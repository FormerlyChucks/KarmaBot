import time, praw, yaml, random, pyimgur, traceback

with open("config.yaml") as config_file:
    config = yaml.safe_load(config_file)
    client_id = config["client_id"]
    client_secret = config["client_secret"]
    user_agent = config["user_agent"]
    username = config["username"]
    password = config["password"]
    imgur_id = config["imgur_id"]
    subs = config["subs"]
    usernames = config["usernames"]

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent, username=username, password=password)

while True:
    try:
        subreddit = reddit.subreddit('random')
        print('Random Subreddit Is: ', subreddit)
        submission = random.choice(list(subreddit.top('all', limit=None)))
        if submission.domain == 'i.redd.it':
            uploaded_image = pyimgur.Imgur(imgur_id).upload_image(url=submission.url)
            reddit.validate_on_submit = True
            subreddit.submit(submission.title, url=uploaded_image.link)
            print('success')
        else: print('domain is not i.redd.it')
    except Exception: print(traceback.format_exc());time.sleep(60)
    except KeyboardInterrupt: print('Shutting Down :(');quit()
