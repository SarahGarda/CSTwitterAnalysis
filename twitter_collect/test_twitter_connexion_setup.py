import pytest

from twitter_collect.twitter_connexion_setup import twitter_setup

def test_twitter_setup():
    connection = twitter_setup()
    assert connection != None
