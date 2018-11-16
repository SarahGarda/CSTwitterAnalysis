import pytest

from twitter_collect.__main__ import *

def test_collection():
    display = collection(1976143068,2)
    assert  display != None
