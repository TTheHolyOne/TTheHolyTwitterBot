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
from tkinter import messagebox, ttk
#from PIL import Image, ImageTk
from twitter import *
import webbrowser



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

window = tk.Tk(className='TTheHolyTwitterBot - V1')
photo = PhotoImage(file = "background.gif")
window.iconphoto(False, photo)
window.geometry('1000x650')


top = Frame(window)
bottom = Frame(window)
bottomm = Frame(window)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, expand=True)


# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):

    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

new = 1
url = "https://www.youtube.com/ttheholyone"

def openwebyt():
    webbrowser.open(url,new=new)
url1 = "https://discord.gg/ebeAytzSeH"

def openwebdiscord():
    webbrowser.open(url1,new=new)



def size_1():
   text.config(font=("Comic Sans MS", 25))

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

def autotwe():
    autots()

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
    text="Authentication OK\nPlease note your keys still may be incorrect | This just means we could connect to twitter api\nIf you get ratelimited wait a few minutes and try again", width=100, height=3
    )
    authmsg.pack()
except:
    errormsg = tk.Label(text="Error Connecting")
    errormsg.pack()

# welcome message

welcome = tk.Label(text="Welcome to TTheHolyTwitterBot! Have Fun!\n", fg="lightcyan")
welcome.pack()


# ALL THE code



# Tweet scraper and analysis button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack()

button1 = tk.Button(
    text="Tweet Scraper and Analysis",
    width=20,
height=2,
bg='#567', fg='White',
justify=CENTER,
padx=10,
borderwidth=0,
command=runscrape

)
button1.pack()

# follow all your followers button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack()

button2 = tk.Button(
    text="Follow all your followers",
width=20,
height=2,
justify=CENTER,
padx=10,
bg='#567', fg='White',
borderwidth=0,
command=followalll
)
button2.pack()

# Tweet button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack()

button3 = tk.Button(
    text="Tweet",
width=20,
height=2,
padx=10,
bg='#567', fg='White',
justify=CENTER,
borderwidth=0,
command=tweetatweet
)
button3.pack()

# Update your status button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack()

button4 = tk.Button(text="Update Your Status", width=20, height=2, bg='#567', fg='White',justify=CENTER, command=statusupdateyeah,borderwidth=0,
 padx=10)
button4.pack()

# Follow a user button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack()

button5 = tk.Button(
    text="Follow a User",
    width=20,
height=2,
padx=10,
bg='#567', fg='White',
justify=CENTER,
borderwidth=0,

command=followaperson
)
button5.pack()

# Blocked Users Button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack()

button6 = tk.Button(
text="See Who You Have Blocked",
width=20,
height=2,
padx=10,
justify=CENTER,
bg='#567', fg='White',
borderwidth=0,

command=blockedusers
)
button6.pack()

# Auto Tweet Button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack()

button7 = tk.Button(
text="Auto Tweeter",
width=20,
height=2,
padx=10,
justify=CENTER,
bg='#567', fg='White',
borderwidth=0,

command=autotwe
)
button7.pack()

# About Button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack()


button8 = tk.Button(
text="About",
width=20,
padx=10,
height=2,
bg='#567', fg='Blue',
borderwidth=0,

justify=CENTER,
command=about
)
button8.pack()
# About Button
seper = tk.Label(text="", borderwidth=0,width=0,height=0)
seper.pack()


button9 = tk.Button(
text="Help",
width=20,
height=2,
bg='#567', fg='Pink',
borderwidth=0,

justify=CENTER,
command=connecthelp
)
button9.pack(in_=bottom, side=LEFT)
# Quit Button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack()
butons = tk.Button(
text=" ",
width=2,
height=2,
borderwidth=0,
justify=CENTER
)
butons.pack(in_=bottom, side=LEFT)
button10 = tk.Button(
text="Quit",
width=20,
height=2,
borderwidth=0,

bg='#567', fg='Red',
justify=RIGHT,
command=quit
)
button10.pack(in_=bottom, side=RIGHT)
butons1 = tk.Button(
text=" ",
width=2,
height=2,
borderwidth=0,
justify=LEFT
)
butons1.pack(side=LEFT)
discord = tk.Button(
text="Discord",
width=20,
height=2,
borderwidth=0,
bg='#567', fg='Red',
justify=LEFT,
command=openwebdiscord
)
discord.pack(side=LEFT)
butons11 = tk.Button(
text=" ",
width=2,
height=2,
borderwidth=0,
justify=RIGHT
)
butons11.pack(side=RIGHT)
youtube = tk.Button(
text="Youtube",
width=20,
height=2,
borderwidth=0,
bg='#567', fg='Red',
justify=RIGHT,
command=openwebyt
)
youtube.pack(side=RIGHT)


changeOnHover(button1, "black", "#567")
changeOnHover(button2, "black", "#567")
changeOnHover(button3, "black", "#567")
changeOnHover(button4, "black", "#567")
changeOnHover(button5, "black", "#567")
changeOnHover(button6, "black", "#567")
changeOnHover(button7, "black", "#567")
changeOnHover(button8, "black", "#567")
changeOnHover(button9, "black", "#567")
changeOnHover(button10, "black", "#567")
changeOnHover(discord, "black", "#567")
changeOnHover(youtube, "black", "#567")


# Starts window
window.mainloop()
