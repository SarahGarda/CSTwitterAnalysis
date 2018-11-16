import pytest

from tweet_text2.textblob_test import *

def test_get_words():
    display = get_words(file)
    assert  display != None
    assert type(display)==list
