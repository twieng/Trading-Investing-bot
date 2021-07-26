#!/usr/bin/env python
# coding: utf-8

# In[17]:


#IF USER IS TOO YOUNG TO PLAY, USER CANNOT PLAY
Name = input("Name: ").upper()
Age = int(input("Age: "))
if Age >= 18:
    print("Hello " + Name + ", you are old enough to play")

    BOT = str(input("Trading Bot (1) / Investing Bot (2): "))
    if BOT == "1":
        print("welcome, you chose trading bot")
        TOTB = input("WHICH TRADING BOT DO YOU WANT? EDDIE/TIN/WARREN: ")
        if TOTB == "eddie":
            print("You chose eddie")
    elif BOT == "2":
        print("you chose INVESTING BOT")
        TOIB = input("WHICH INVESTING BOT DO YOU WANT? EDDIE/TIN/WARRN: ")
        if TOIB == "eddie":
            print("you chose Eddie's Investment Bot")
    else:
        print("Sorry, there are only 2 options")

else:
    print("Sorry " + Name + ", you are too young to play")
    quit()


# In[ ]:




