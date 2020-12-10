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
            with open ('links.txt', "a") as f:
                f.write(uploaded_image.link + "\n")
            reddit.validate_on_submit = True
            subreddit.submit(submission.title, url=uploaded_image.link)
            print('success')
        else: print('domain is not i.redd.it')
        for submission in reddit.subreddit(subs).stream.submissions(skip_existing=True):
            for results in subreddit.search(submission.title): 
                if results.num_comments >= 3 and difflib.SequenceMatcher(None, submission.title,results.title).ratio() >= .8:
                    comment = results.comments[random.randint(0,2)]
                    if comment.author not in usernames and comment.body != '[deleted]':
                        submission.reply(comment.body)
                        break   
    except Exception: print(traceback.format_exc());time.sleep(60)
    except KeyboardInterrupt: print('Shutting Down :(');quit()
