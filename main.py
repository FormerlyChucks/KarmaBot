import time, praw, yaml, random, pyimgur, traceback

with open("config.yaml") as cf:
    config = yaml.safe_load(cf)
    _id = cf["client_id"]
    secret = cf["client_secret"]
    agent = cf["user_agent"]
    username = cf["username"]
    password = cf["password"]
    imgur_key = cf['imgur_id']

reddit = praw.Reddit(client_id=_id,
                     client_secret=secret,
                     user_agent=agent,
                     username=username,
                     password=password)

reddit.validate_on_submit = True

def upload(imgur_id,url):
    img = pyimgur.Imgur(imgur_id)
    image = img.upload_image(url=url)
    return image.link
    
def submit(title,url):
    subreddit.submit(title,url)
    return 'success'

while True:
    try:
        subreddit = reddit.subreddit('random')
        print('Random Subreddit Is: ',subreddit)
        submissions = list(subreddit.top('all', limit=None))
        submission = random.choice(submissions)
        if submission.domain == 'i.redd.it':
            link = upload(imgur_id=imgur_key)
            post = submit(title, url=link)
            print(post)
        else:
            print('domain is not i.redd.it')
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
    except KeyboardInterrupt:
        print('Shutting Down :(')
        quit()
