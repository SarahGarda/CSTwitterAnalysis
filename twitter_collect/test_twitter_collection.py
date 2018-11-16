import pytest

from twitter_collect.twitter_collection import *

def test_collect():
    collection = collect()
    assert collection != None



def test_collect_by_user():
    collection = collect_by_user(1976143068)
    #the function is tested with Macron's user id
    assert collection != None

def test_collect_by_streaming():
    stream_collect = twitter_setup()
    assert stream_collect != None
