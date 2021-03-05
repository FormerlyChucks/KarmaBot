import time, praw, yaml, random, pyimgur, traceback

with open("config.yaml") as config_file:
    config = yaml.safe_load(config_file)

reddit = praw.Reddit(client_id=config["client_id"],
                     client_secret=config["client_secret"],
                     user_agent=config["user_agent"],
                     username=config["username"],
                     password=config["password"])

reddit.validate_on_submit = True

while True:
    try:
        subreddit = reddit.subreddit('random');print('Random Subreddit Is: ',subreddit)
        submissions = list(subreddit.top('all', limit=None));submission = random.choice(submissions)
        if submission.domain == 'i.redd.it': subreddit.submit(submission.title, url=pyimgur.Imgur(config["imgur_id"]).upload_image(url=submission.url).link);print('success')
        else: print('domain is not i.redd.it')
    except Exception: print(traceback.format_exc());time.sleep(60)
    except KeyboardInterrupt: print('Shutting Down :(');quit()
