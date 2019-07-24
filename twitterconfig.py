# tweepy-bots/bots/config.py
import logging

import tweepy

logger = logging.getLogger()


def create_api():
    consumer_key = "4nvrptB22arTA5EBL5X47WvuJ"
    consumer_secret = "D4G29umhN8G0UUYGliatlyk3g2fxibHI12eBR0cjbyUPUBTFqm"
    access_token = "1151467552616407041-ernUY2ORTrQFKyXghSv6w2Tp6fjk2Z"
    access_token_secret = "dtnu0Wjd0MXGPGJAzF3Jm9AxLu44SFg5ZCy48vN9b31WU"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
        print("autenticou show")
    except:
        print("deu ruim")

    return api
