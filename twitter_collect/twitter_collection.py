from credentials import *
from twitter_collect.twitter_connexion_setup import *


def collect():
    connexion = twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)

print(collect())
