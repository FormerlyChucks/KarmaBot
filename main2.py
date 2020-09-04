import praw
import time
import config
import difflib
 
reddit = praw.Reddit(client_id=config.C_ID, client_secret=config.C_S, user_agent=config.U_A, username=config.UN, password=config.PW)

bad_subs = ['rape', 'abuse', 'more', 'subs', 'to', 'ignore']
bad_users = ['diogenesjunior', 'diogenesjunior2', 'GallowTits', 'more', 'users', 'to', 'ignore']
subreddit = reddit.subreddit('random')

while True:
    try:
        
        for submission in subreddit.new(limit=1):
            if submission.subreddit not in bad_subs:
                for search in subreddit.search(submission.title):
                    similarity = difflib.SequenceMatcher(None, submission.title, search.title).ratio()
                    our_comment = search.comments[0]
                    stickied = our_comment.stickied
                    comment_author = our_comment.author
                    if similarity >= .9 and stickied == False and comment_author not in bad_users:
                        submission.reply(our_comment.body)
                        
    except Exception as e:
        print(e)
        time.sleep(60)
        
    except KeyboardInterrupt:
        spinner.warn(text='shutting down :(')
        quit()