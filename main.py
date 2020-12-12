import time, praw, yaml, random, pyimgur, traceback

with open("config.yaml") as config_file:
    config = yaml.safe_load(config_file)
    client_id = config["client_id"]
    client_secret = config["client_secret"]
    user_agent = config["user_agent"]
    username = config["username"]
    password = config["password"]
    imgur_id = config["imgur_id"]

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,password=password)

reddit.validate_on_submit = True

while True:
    try:
        subreddit = reddit.subreddit('random')
        print('Random Subreddit Is: ', subreddit)
        submissions = list(subreddit.top('all', limit=None))
        submission = random.choice(random.choice(submissions))
        if submission.domain == 'i.redd.it':
            im = pyimgur.Imgur(imgur_id)
            im.upload_image(url=submission.url)
            subreddit.submit(submission.title, url=uploaded_image.link)
            print('success')
        else:
            print('domain is not i.redd.it')
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
    except KeyboardInterrupt:
        print('Shutting Down :(')
        quit()
