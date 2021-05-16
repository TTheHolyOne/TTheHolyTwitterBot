'''
TTheHolyone's Twitter Bot
Credits:
github.com/TTheHolyOne
ttheholyone.com
TTheHolyOne#1642

My Twitter Bot

This bot is a cool bot that I find awesome!

To get started
download holytwitter.py on this github NOTE:  you already have
now go into the directory the file is on in command prompt
now you need to install the packages
which are these commands here:

pip install tweepy
pip install pandas
pip install textblob

now to get it up and running on your account you need to make a developer account for twitter
To get it make a developer account on:
https://developer.twitter.com/en/portal/projects-and-apps\
now create a app
and now go into the settings of the app and find the api keys and then put it where it says to put it in the code
Now go to command prompt and go to the folder where the holytwitter.py is located and type holytwitter.py
Enjoy!

'''
#Important
import tweepy
import os
import sys
import pandas as pd
import time
from textblob import TextBlob
import sys
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from twitter import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


window = tk.Tk(className='TTheHolyTwitterBot')
window.geometry('1000x500')
window.configure(bg= "#37F3CC")

def runscrape():
    scrapestuff()

def followalll():
    followfollowers()

def tweetatweet():
    tweetstuffg()

def statusupdateyeah():
    statusstuff()

def followaperson():
    followauser()

def blockedusers():
    blocks()

def about():
    return messagebox.showinfo('About TTheHolyTwitterBot:',"""
Developer:
TTheHolyOne#1642

This is a bot where you can do fun stuff!
It is constantly updated and I quite enjoy it.
You can change your status, follow, tweet, follow all followers, track tweets, see blocked users etc!

VERSION 2
""")

def connecthelp():
    return messagebox.showinfo('How to Connect to Tweepy API:',"""
Hello!
I'm TTheHolyOne the developer of this program!
I heard you need help connecting to tweepy's api!
Its super easy!

First create a twitter account if you don't have one already

Done? Great!

Now go to this website:

https://developer.twitter.com/en/portal/projects-and-apps

and sign up for a Twitter Developer account

Once done create a app

and once you create the app go inside of the settings in the app and find your api keys!

now go to twitter.py and where it says put your api keys here put them there!

There are plenty of tutorials online if you are stuck :D
""")



# sees if it can connect to twitter api

try:
    api.verify_credentials()
    authmsg = tk.Label(
    text="Authentication OK\nPlease note your keys still may be incorrect\nThis just means we could connect to twitter api", width=100, height=3
    )
    authmsg.pack()
except:
    errormsg = tk.Label(text="Error Connecting")
    errormsg.pack()

# welcome message

welcome = tk.Label(text="Welcome to TTheHolyTwitterBot! Have Fun!\n")
welcome.pack()




# ALL THE code


# Tweet scraper and analysis button

button1 = tk.Button(
    text="Tweet Scraper and Analysis",
    width=20,
height=2,
bg='#567', fg='White',
justify=CENTER,
command=runscrape
)
button1.pack()

# follow all your followers button

button2 = tk.Button(
    text="Follow all your followers",
width=20,
height=2,
justify=CENTER,
bg='#567', fg='White',
command=followalll
)
button2.pack()

# Tweet button

button3 = tk.Button(
    text="Tweet",
width=20,
height=2,
bg='#567', fg='White',
justify=CENTER,
command=tweetatweet
)
button3.pack()

# Update your status button

button4 = tk.Button(text="Update Your Status", width=20, height=2, bg='#567', fg='White',justify=CENTER, command=statusupdateyeah)
button4.pack()

# Follow a user button

button5 = tk.Button(
    text="Follow a User",
    width=20,
height=2,
bg='#567', fg='White',
justify=CENTER,
command=followaperson
)
button5.pack()

# Blocked Users Button

button6 = tk.Button(
text="See Who You Have Blocked",
width=20,
height=2,
justify=CENTER,
bg='#567', fg='White',
command=blockedusers
)
button6.pack()

# About Button


button7 = tk.Button(
text="About",
width=20,
height=2,
bg='#567', fg='Blue',
justify=CENTER,
command=about
)
button7.pack()
# About Button


button8 = tk.Button(
text="Help",
width=20,
height=2,
bg='#567', fg='Pink',
justify=CENTER,
command=connecthelp
)
button8.pack()

# Quit Button

button8 = tk.Button(
text="Quit",
width=20,
height=2,
bg='#567', fg='Red',
justify=CENTER,
command=quit
)
button8.pack()




# Starts window
window.mainloop()
