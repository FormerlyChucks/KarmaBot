import praw, yaml, random, pyimgur

with open("config.yaml") as cf:
    config = yaml.safe_load(cf)

reddit = praw.Reddit(client_id=config["client_id"],
                     client_secret=config["client_secret"],
                     user_agent=config["user_agent"],
                     username=config["username"],
                     password=config["password"])

reddit.validate_on_submit = True
img = pyimgur.Imgur(config['imgur_id'])
subreddit = reddit.subreddit('random')
print('Random Subreddit Is:',subreddit.display_name)
post = random.choice([submission for submission in list(subreddit.top('all', limit=None)) if submission.domain == 'i.redd.it'])
print('Random Submission from /r/'+subreddit.display_name,'is:',post.id)
image = img.upload_image(url=post.url)
submit = subreddit.submit(title,url=image.link)
print('Repost located here:',submit.url)
