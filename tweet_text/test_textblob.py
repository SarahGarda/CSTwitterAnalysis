import textblob
form twitter_collect.twitter_collection import *

file=collect()

def get_words(file):
    words=[]
    for tweet in file:
        interm_words=[]
        wiki=TextBlob(str(tweet.txt))
        for w in wiki.words:
            interm_words.append(w.lemmatize())
        words+=inter_words
    return(words)
