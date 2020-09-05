import praw
import random
import time
import config
from difflib import SequenceMatcher

reddit = praw.Reddit(client_id=config.C_ID, client_secret=config.C_S, user_agent=config.U_A, username=config.UN, password=config.PW)

cache=[]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
def grab_reply():
    submission_ids = [] 
    x=0
    subreddit = reddit.subreddit("random")
    for submission in subreddit.hot(limit=1):
        question_id = submission.id
        question = submission.title
        comments = submission.num_comments
        previous=0
        for ids in cache:
            if question_id == ids:
                previous=1
            if previous == 1:
                break
                return
        cache.append(question_id)
        print(question)
        for results in subreddit.search(question):
            id = results.id
            title = results.title
            comments = results.num_comments
            if comments > 10 and similar(question,title) > .8:
                submission_ids.append(id)
                x += 1
            if x >=10:
                break
        if len(submission_ids) == 0:
            return
        submission = reddit.submission(id=submission_ids[random.randint(0,len(submission_ids)-1)])
        comment_list=[]
        x=0
        for top_level_comment in submission.comments:
            body = top_level_comment.body
            comment_list.append(body)
            x += 1
            if x >=5:
                break
        if len(comment_list) == 0:
            return
    comment_reply = comment_list[random.randint(0,len(comment_list)-1)]
    if comment_reply == "[deleted]":
        return
    submission = reddit.submission(id=question_id)
    submission.reply(comment_reply)
    return comment_reply

while 1:
    time.sleep(30)