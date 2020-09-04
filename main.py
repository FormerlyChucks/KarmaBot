import time
import praw
import random
import config
import pyimgur
from halo import Halo

spinner = Halo(spinner={'interval': 100, 'frames': ['-', '+', '*', '+', '-']})

reddit = praw.Reddit(client_id=config.C_ID, client_secret=config.C_S, user_agent=config.U_A, username=config.UN, password=config.PW)
imgur_id = config.I_ID
bad_subs = ['rape', 'abuse', 'more', 'subs', 'to', 'ignore']

while True:
    try:
        spinner.start()
        subreddit = reddit.subreddit('random')
        domains = ['i.redd.it', 'i.imgur.com']
        limit = None
        print('Random Subreddit Is: ', subreddit)
        
        submissions = list(subreddit.top('all', limit=limit))
        submission = random.choice(submissions)
        if subreddit not in bad_subs and submission.domain in domains:
            im = pyimgur.Imgur(imgur_id)
            uploaded_image = im.upload_image(url=submission.url)
            with open ('links.txt', "a") as f:
                f.write(uploaded_image.link + "\n")
            reddit.validate_on_submit = True
            subreddit.submit(submission.title, url=uploaded_image.link)
            spinner.succeed('success')
            
        elif submission.domain not in domains:
            spinner.info('domain is not in domains :(')
            
    except Exception as e:
        exc = str(str(e))
        spinner.fail(text=exc)
        time.sleep(60)
        
    except KeyboardInterrupt:
        spinner.warn(text='shutting down :(')
        quit()
