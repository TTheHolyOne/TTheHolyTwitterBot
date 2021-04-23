'''
TTheHolyone's Twitter Bot
Credits:
github.com/TTheHolyOne
ttheholyone.com
TTheHolyOne#1642

My Twitter Bot
'''
#Important
import tweepy
import pandas as pd
import time
from textblob import TextBlob
import sys
import random

#Very important or bot wont work
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
# Very Important
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#creating a list of tweets

tweets = []
print('Hello there!\nWelcome to TTheHolyTwitterBot!')
def twitterbotoptions():
    options = input('\n\n1: Tweet Scraper and Analysis\n2: Follow all your followers\n3: Quit\n')
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
        sys.exit()
twitterbotoptions()
print('Shutting down..')
