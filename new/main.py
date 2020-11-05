import time, praw, random, config, pyimgur

reddit = praw.Reddit(client_id=config.C_ID, client_secret=config.C_S, user_agent=config.U_A, username=config.UN, password=config.PW)
reddit.validate_on_submit = True

while True:
    try:
        submission = random.choice(list(reddit.subreddit('random').top('all', limit=None)))
        if submission.domain in ['i.redd.it', 'i.imgur.com']:
            uploaded_image = pyimgur.Imgur(config.I_ID).upload_image(url=submission.url)
            subreddit.submit(submission.title, url=uploaded_image.link)
            time.sleep(60)
        elif submission.domain not in domains: time.sleep(60)
        for submission in reddit.subreddit(config.SUBS).stream.submissions(skip_existing=True):
            for results in subreddit.search(submission.title): 
                similarity = difflib.SequenceMatcher(None, submission.title,results.title).ratio()
                if results.num_comments >= 3 and similarity >= .8:
                    comment = results.comments[random.randint(0,2)]
                    if comment.author not in config.usernames and comment.body != '[deleted]':
                        submission.reply(comment.body)
                        break           
    except Exception: time.sleep(60)       
    except KeyboardInterrupt: quit()
