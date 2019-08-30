from reddit import create_api
import glob
import os
import time
import urllib.request
from random import randint

Reddit = create_api()
subreddit = Reddit.subreddit('hentai')

while True:
    newPost = subreddit.new(limit=1)

    for submission in newPost:
        if submission.url is not None:
            urlImagem = submission.url

    files = glob.glob('./img/*')
    for f in files:
        os.remove(f)

    imgDir = "./img/00000001.jpg"
    urllib.request.urlretrieve(urlImagem, imgDir)