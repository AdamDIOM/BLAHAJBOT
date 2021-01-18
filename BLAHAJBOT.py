import praw
import requests
import shutil
from urllib.parse import urlencode
import webbrowser
import time
import pyautogui
from hashlib import sha256
import random


r = praw.Reddit(
    client_id = "tlWQbv1dK0aJrQ",
    client_secret = "jhU_gLgLNdTVLhb0Eb6eKC74tzSCOg",
    user_agent = "USERAGENT"
    )
print(1)

# Doing this for the memes
if True:
    memes = r.subreddit("memes+dankmemes+darkmemes")
    listofmemes = memes.top('year', limit = 1000)
    count = 0
    memeUrlList = []
    memeCommentList = []
    listCompleted = []
    print(2)
    for submission in listofmemes:
        memeUrlList.append(submission.url)
        memeCommentList.append(submission.title)
        print(len(memeUrlList))
    print(3)
    for submission in memeUrlList:
        print(4)
        n = random.randint(0,999)
        while n in listCompleted:
            n = random.randint(0,999)
        listCompleted.append(n)
        count += 1
        print(5)
        requests.post('https://discord.com/api/webhooks/800155967118376970/7MXNuSJmNBxn4lfAm0VKkWD1fVw_DL_qu5ZbiHrWo3JUn0X8X9powPf7_510cdu43c5g', data = {'content': memeCommentList[n]})
        print(6)
        requests.post('https://discord.com/api/webhooks/800155967118376970/7MXNuSJmNBxn4lfAm0VKkWD1fVw_DL_qu5ZbiHrWo3JUn0X8X9powPf7_510cdu43c5g', data = {'content': memeUrlList[n]})
        print(7)
        #print(submission.url)
        time.sleep(5)
        if count % 10 == 0:
            time.sleep(600)

        # Open the url image, set stream to True, this will return the stream content.
        #r = requests.get(submission.url, stream = True)

        # Check if the image was retrieved successfully
        #if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            #r.raw.decode_content = True
            

while(True):
    time.sleep(10)
    link = "link goes here"
    #requests.post('https://discord.com/api/webhooks/800155967118376970/7MXNuSJmNBxn4lfAm0VKkWD1fVw_DL_qu5ZbiHrWo3JUn0X8X9powPf7_510cdu43c5g', data = {'content': link})
