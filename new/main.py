import time, praw, random, config, pyimgur, traceback

reddit = praw.Reddit(client_id=config.C_ID, client_secret=config.C_S, user_agent=config.U_A, username=config.UN, password=config.PW)
reddit.validate_on_submit = True
x = random.randint(0,2)

while True:
    try:
        subreddit = reddit.subreddit('random')
        print('Random Subreddit Is: ', subreddit)       
        submissions = list(subreddit.top('all', limit=None))
        submission = random.choice(submissions)
        if submission.domain in ['i.redd.it', 'i.imgur.com']:
            im = pyimgur.Imgur(config.I_ID)
            uploaded_image = im.upload_image(url=submission.url)
            with open ('links.txt', "a") as f:
                f.write(uploaded_image.link + "\n")
            subreddit.submit(submission.title, url=uploaded_image.link)
            print('success')
            time.sleep(60)
        elif submission.domain not in domains:
            print('domain is not in domains :(')
            time.sleep(60)
        for submission in reddit.subreddit(config.SUBS).stream.submissions(skip_existing=True):
            for results in subreddit.search(submission.title): 
                similarity = difflib.SequenceMatcher(None, submission.title,results.title).ratio()
                if results.num_comments >= 3 and similarity >= .8:
                    comment = results.comments[x]
                    if comment.author not in config.usernames and comment.body != '[deleted]':
                        submission.reply(comment.body)
                        break
            
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
        
    except KeyboardInterrupt:
        print('shutting down :(')
        quit()
