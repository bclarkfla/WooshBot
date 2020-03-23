#!/usr/bin/python3
import praw
from datetime import datetime

reddit = praw.Reddit('HelloImWoosh')
subreddit = reddit.subreddit("doughboys")

def main():
    comments = subreddit.comments(limit=400)
    currentDate = datetime.utcnow().strftime('%m-%d')
    currentYear = datetime.utcnow()
    recentUsers = []
    for comment in comments:
        rName = comment.author.name
        if rName not in recentUsers:
            cakeday = get_cakeday(rName,currentYear)
            recentUsers.append(rName)
            if cakeday == currentDate:
                print("{}, {}, {} !!!".format(rName,cakeday,currentDate))
                comment.reply("[Hey you! Happy Birthday! You're Cool!](https://youtu.be/Y6JnYnA9Tzo)")
            else:
                print("{}, {}, {}".format(rName,cakeday,currentDate))
            
            
def get_cakeday(rName,currentYear):
    cakeday = reddit.redditor(rName).created_utc
    cakeday = datetime.utcfromtimestamp(cakeday)
    if cakeday.year != currentYear.year:
        cakeday = cakeday.strftime('%m-%d')
    else:
        cakeday = cakeday.strftime('%Y-%m-%d')
    return(cakeday)
    
def lambda_handler(event, context):
    main()
