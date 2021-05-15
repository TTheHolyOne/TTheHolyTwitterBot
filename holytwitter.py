'''
TTheHolyone's Twitter Bot
Credits:
github.com/TTheHolyOne
ttheholyone.com
TTheHolyOne#1642

My Twitter Bot

This bot is a cool bot that I find awesome!
'''
#Important
import tweepy
import pandas as pd
import time
from textblob import TextBlob
import sys
import random

#user credentials to authenticate API
#you will get these credentilas when creating a developer account on Twitter
consumer_key = "Your Key Here"
consumer_secret = "Your Key Here"
access_token = "Your Key Here"
access_token_secret = "Your Key Here"
# Very Important
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#creating a list of tweets

tweets = []
print('Hello there!\nWelcome to TTheHolyTwitterBot!')

def twitterbotoptions():
    options = input("""

OPTIONS:

1: Tweet Scraper and Analysis\n
2: Follow all your followers\n
3: Tweet\n
4: Update your status\n
5: Quit\n
""")
    time.sleep(1)
    if options == '1':
        print('Okay lets do this!\n\n')
        #specify whose tweets you're scraping
        usernameinput = input('\nWhat is the username of the twitter user you want to scrape tweets from?(CAPSLOCK SENSITIVE)\n\n')
        username = f'{usernameinput}'
        #number of tweets you need
        tweets_numinput = int(input('How many tweets would you like to scrape from this user?\n\n'))
        tweets_num = tweets_numinput
        time.sleep(1)
        public_tweets = api.search({usernameinput})


        blank = ' '
        for tweet in public_tweets:
            print(tweet.text)


            #Step 4 Perform Sentiment Analysis on Tweets
            analysis = TextBlob(tweet.text)
            print(analysis.sentiment)
        print('Time to scrape..... Wait for it to be finished\n')
        numbers = random.randint(1,1000)

        #defining a converting function which takes username and count as parameters
        def tweets_to_csv(username,tweets_num):

                #getting the individual tweets
                for tweet in api.user_timeline(id=username, count=tweets_num):

                    #adding tweets to the list
                    tweets.append((tweet.created_at,tweet.id,tweet.text,blank,analysis.sentiment))

                    #creating a dataframe in pandas and defining column names
                    df = pd.DataFrame(tweets,columns=['Date', 'Tweet_ID', 'Message', '\n', '\nAnalysis'])

                    #converting dataframe to CSV file
                    df.to_csv(f'{username}_scraped_tweets_{str(numbers)}.csv')


        #calling the function to create the CSV file
        tweets_to_csv(username, tweets_num)
        print(f'Successfully scrapped {tweets_num} tweets from {username}\nCheck the folder of this script for the .csv file!\nMade by TTheHolyOne')
        time.sleep(2)
        twitterbotoptions()
    elif options == '2':
        print('Okay whatever you say! :D ')
        for follower in tweepy.Cursor(api.followers).items():
            follower.follow()
        print(f'Done')
        twitterbotoptions()
    elif options == '3':
        tweetstuff = input("Please enter a string of text you would like to tweet: \n")
        api.update_status(f"{tweetstuff}")
        twitterbotoptions()
    elif options == '4':
        tweetstatus = input("Please choose a status you want: \n")
        api.update_profile(description=f"{tweetstatus}")
        twitterbotoptions()
    elif options == '5':
        print("Goodbye!")
        time.sleep(1)
        sys.exit()
twitterbotoptions()
print('Shutting down..')
