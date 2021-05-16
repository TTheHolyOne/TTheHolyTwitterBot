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
from random import randint
import colorama
from colorama import *

init()

#user credentials to authenticate API
#you will get these credentilas when creating a developer account on Twitter
consumer_key = "YOUR KEY HERE WATCH https://www.youtube.com/watch?v=0VsyRO8Z9u4 TO FIND OUT HOW TO GET IT"
consumer_secret = "YOUR KEY HERE WATCH https://www.youtube.com/watch?v=0VsyRO8Z9u4 TO FIND OUT HOW TO GET IT"
access_token = "YOUR KEY HERE WATCH https://www.youtube.com/watch?v=0VsyRO8Z9u4 TO FIND OUT HOW TO GET IT"
access_token_secret = "YOUR KEY HERE WATCH https://www.youtube.com/watch?v=0VsyRO8Z9u4 TO FIND OUT HOW TO GET IT"
# Very Important
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#creating a list of tweets

tweets = []
print(Fore.RED + 'Hello there!\nWelcome to TTheHolyTwitterBot!\nPlease wait for GUI to open...')


def autots():
    print("This will tweet out and change your status infinitely until you close this window\n\n")
    timeperchange = int(input("Please choose a number for time before every change: \n"))
    timeperchange2 = int(input("Please choose another number for time before every change: \n"))
    print(f"Your status and tweet will tweet every "+str(timeperchange)+" - "+str(timeperchange2)+ " seconds")
    messageuser = input("Please choose a message to tweet out every "+str(timeperchange)+" - "+str(timeperchange2)+" seconds: \n")
    funtweetstatus = input("\n\nPlease choose a status to change every "+str(timeperchange)+" - "+str(timeperchange2)+" seconds: \n")
    input("Okay...\nClose this window to stop the tweets and status change\n\nPress enter to proceed")
    timerr = 0
    try:
        while True:
            randomtime = randint(timeperchange, timeperchange2)
            print(randomtime)
            time.sleep(randomtime)
            timerr +=1
            api.update_status(f"{messageuser}\n\nFun Fact: I have tweeted this "+str(timerr)+" times!")
            api.update_profile(description=f"{funtweetstatus}\n\nFun Fact: I have changed this status "+str(timerr)+" times!")
    except:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\nIt seems that you are being ratelimited...\nTry auto tweeter again later")
        time.sleep(3)
        sys.exit()

def scrapestuff():
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

def followfollowers():
    print('Okay whatever you say! :D ')
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
    print(f'Done')

def tweetstuffg():
    tweetstuff = input("Please enter a string of text you would like to tweet: \n")
    api.update_status(f"{tweetstuff}")

def statusstuff():
    tweetstatus = input("Please choose a status you want: \n")
    api.update_profile(description=f"{tweetstatus}")

def followauser():
    folowuser = input("Please enter a twitter username to follow: \n")
    api.create_friendship(f"{folowuser}")

def blocks():
    print("BLOCKED USERS: \n\n")
    for block in api.blocks():
        print(block.name)
