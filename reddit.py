import praw
import pandas as pd
import os 

username = "Working_Song8171"
password = 'password1234'
client_id = '7cCDsGLtpcFqgksYpsGfCg'
client_secret = 'zbSHdg-FsyNR3ZUf3xyBS9UXPjFQvQ'
subreddit_name = 'wholesomestories'

user_agent = "praw_scraper_1.0"

# Create an instance of reddit class
reddit = praw.Reddit(username=username,
                     password=password,
                     client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent
)

subreddit = reddit.subreddit(subreddit_name)

titles = []
scores = []
ids = []
sentences_total = []

for i,submission in enumerate(subreddit.hot(limit = 100)):
    if (i == 0):
        continue
    titles.append(submission.title)
    scores.append(submission.score)
    ids.append(submission.id)
    no_zero_ws = submission.selftext.replace('&#x200B;', '').replace('\n', '').replace('fuck', 'f').replace('ass', 'a').replace('shit','crap').replace('dead', 'unalived').replace('kill', 'unalive').replace('suicide', 'unalive').replace('dick', 'd').split(' ')
    sentence = [' '.join(no_zero_ws[i:i+10]) for i in range(0,len(no_zero_ws),10)]
    if not os.path.exists(f"text_files/{subreddit_name}"):
        os.makedirs(f"text_files/{subreddit_name}")
                      
    f = open(f"text_files/{subreddit_name}/{submission.id}.txt", "a")
    for i in sentence:   
        f.write(i)
        f.write('\n')
    f.close()

    
df = pd.DataFrame({'id': ids, 'title': titles, 'score': scores})

df.to_csv(f'csvs/{subreddit_name}.csv')