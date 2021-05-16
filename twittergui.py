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
consumer_key = "put api key here"
consumer_secret = "put api key here"
access_token = "put api key here" 
access_token_secret = "put api key here"
# Very Important
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

window = tk.Tk(className='TTheHolyTwitterBot - V1')
photo = PhotoImage(file = "background.gif")
window.iconphoto(False, photo)
window.geometry('1000x300')
window.configure(bg='#0b132b')


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
    text="\n\n\nAuthentication OK\nPlease note your keys still may be incorrect | This just means we could connect to twitter api\nIf you get ratelimited wait a few minutes and try again",
    width=100,
    height=7,
    justify=CENTER,
bg='#0b132b',
fg='#3a506b',
    borderwidth = 0,
    )
    authmsg.pack()
except:
    errormsg = tk.Label(text="Error Connecting")
    errormsg.pack()

# welcome message

welcome = tk.Label(text="Welcome to TTheHolyTwitterBot! Have Fun!\n", bg='#0b132b',fg="#8C81D4",borderwidth=0,)
welcome.pack()


# ALL THE code



# Tweet scraper and analysis button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack(in_=bottom, side=RIGHT)

button1 = tk.Button(
    text="Scraper & Analysis",
width = 16,
height=2,
bg='#3a506b', fg='White',
justify=CENTER,
padx=10,
borderwidth=1,
command=runscrape

)
button1.pack(in_=bottom, side=RIGHT)

# follow all your followers button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack(in_=bottom, side=RIGHT)

button7 = tk.Button(
text="Auto Tweeter",
width = 15,
height=2,
padx=10,
justify=CENTER,
bg='#3a506b', fg='White',
borderwidth=1,

command=autotwe
)
button7.pack(in_=bottom, side=RIGHT)
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack(in_=bottom, side=RIGHT)
button3 = tk.Button(
    text="Tweet",
width = 15,
height=2,
padx=10,
bg='#3a506b', fg='White',
justify=CENTER,
borderwidth=1,
command=tweetatweet
)
button3.pack(in_=bottom, side=RIGHT)
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack(in_=bottom, side=RIGHT)
button2 = tk.Button(
    text="Follow your Followers",
width = 15,
height=2,
justify=CENTER,
padx=10,
bg='#3a506b', fg='White',
borderwidth=1,
command=followalll
)
button2.pack(in_=bottom, side=RIGHT)
# Update your status button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack(in_=bottom, side=RIGHT)
button5 = tk.Button(
    text="Follow a User",
width = 15,
height=2,
padx=10,
bg='#3a506b', fg='White',
justify=CENTER,
borderwidth=1,

command=followaperson
)
button5.pack(in_=bottom, side=RIGHT)
# Blocked Users Button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack(in_=bottom, side=RIGHT)

button6 = tk.Button(
text="Blocked Users",
width = 15,
height=2,
padx=10,
justify=CENTER,
bg='#3a506b', fg='White',
borderwidth=1,

command=blockedusers
)
button6.pack(in_=bottom, side=RIGHT)

seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack(in_=bottom, side=RIGHT)

button4 = tk.Button(text="Update Status", width = 15, height=2, bg='#3a506b', fg='White',justify=CENTER, command=statusupdateyeah,borderwidth=1,
 padx=10)
button4.pack(in_=bottom, side=RIGHT)


# Auto Tweet Button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack(in_=bottom, side=RIGHT)



butons1 = tk.Button(
text="",
width=2,
height=2,
padx=0,
borderwidth=0,
justify=LEFT,
bg="#0b132b",
)
butons1.pack(in_=top, side=LEFT)
discord = tk.Button(
text="Discord",
width=20,
height=2,
bg='#3a506b', fg='Red',
justify=LEFT,
command=openwebdiscord
)
discord.pack(in_=top, side=LEFT)
butons11 = tk.Button(
text=" ",
width=2,
height=2,
borderwidth=0,
bg="#0b132b",
justify=RIGHT
)
butons11.pack(in_=top, side=LEFT)

# About Button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack(in_=bottom, side=RIGHT)


button9 = tk.Button(
text="Help",
width=20,
height=2,
bg='#3a506b', fg='#49A078',
justify=CENTER,
command=connecthelp
)
button9.pack(in_=top, side=LEFT)
# Quit Button
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack()
butons = tk.Button(
text="",
width=2,
height=2,
bg="#0b132b",
borderwidth=0,
justify=CENTER
)
butons.pack(in_=top, side=LEFT)
button10 = tk.Button(
text="Quit",
width=20,
height=2,
bg='#3a506b', fg='Red',
justify=LEFT,
command=quit
)
button10.pack(in_=top, side=LEFT)
seper = tk.Label(text="\n", borderwidth=0,width=0,height=1)
seper.pack()
butonss = tk.Button(
text=" ",
width=2,
height=2,
bg="#0b132b",
borderwidth=0,
justify=CENTER
)
butonss.pack(in_=top, side=LEFT)
button8 = tk.Button(
text="About",
width=20,
padx=10,
height=2,
bg='#3a506b', fg='#49A078',
justify=LEFT,
command=about
)
button8.pack(in_=top, side=LEFT)

butonsss = tk.Button(
text=" ",
width=2,
height=2,
bg="#0b132b",
borderwidth=0,
justify=CENTER
)
butonsss.pack(in_=top, side=LEFT)

youtube = tk.Button(
text="Youtube",
width=20,
height=2,
bg='#3a506b', fg='Red',
justify=RIGHT,
command=openwebyt
)
youtube.pack(in_=top, side=RIGHT)


changeOnHover(button1, "black", "#3a506b")
changeOnHover(button2, "black", "#3a506b")
changeOnHover(button3, "black", "#3a506b")
changeOnHover(button4, "black", "#3a506b")
changeOnHover(button5, "black", "#3a506b")
changeOnHover(button6, "black", "#3a506b")
changeOnHover(button7, "black", "#3a506b")
changeOnHover(button8, "black", "#3a506b")
changeOnHover(button9, "black", "#3a506b")
changeOnHover(button10, "black", "#3a506b")
changeOnHover(discord, "black", "#3a506b")
changeOnHover(youtube, "black", "#3a506b")

# Starts window
window.mainloop()
