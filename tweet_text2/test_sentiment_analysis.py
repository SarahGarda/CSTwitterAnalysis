import pytest

from tweet_text2.sentiment_analysis import *
from twitter_collect.twitter_collection import *


def test_sentiment_percentage():
    display = sentiment_percentage(collect())
    assert  display != None
    assert type(display)==list
