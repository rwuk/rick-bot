from twython import TwythonStreamer
from twython import Twython
import random
import time

while 10 == 10:

    from auth import (
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


messages = [
    "Wubbalubbadubdub!",
    "Rikitikitavi bitch!",
    "And that's the wayyyyyy the news goes!",
    "Hit the sack, Jack!",
    "Uh ohhhh! Somersoult jump!",
    "AIDS!",
    "And that's why I always say, 'Shumshumschilpiddydah!'",
    "GRASSSSS... tastes bad!",
    "No jumping in the sewer.",
    "BURGERTIME!",
    "Rubber baby buggy bumpers!",
    "Lick, lick, lick, my BALLS!",
]


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = random.choice(messages)
            x =("@%s: %s" % (username, tweet))
            print x
            twitter.update_status(status=x)
            print("Tweeted: %s" % x)
            time.sleep(180)

stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

stream.statuses.filter(track='Rick and Morty')


