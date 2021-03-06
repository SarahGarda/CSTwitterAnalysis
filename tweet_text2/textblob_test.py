from textblob import *
import tweepy
import nltk
from credentials import *
from twitter_collect.twitter_connexion_setup import *
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

#we rewrite collec because we had an importation problem from twitter_collect
def collect():
    connexion = twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=100)
    #for tweet in tweets:
        #print(tweet.text)
    return(tweets)

file=collect()

def get_words(file):
    '''
    :param file: the file to analyze
    :return: the list of lemmatized words in file excluding the most commonly used ones.
    '''
    words=[]
    for tweet in file:
        interm_words=[]
        wiki=TextBlob(str(tweet.text))
        for w in wiki.words:
            if w not in stopwords.words('french'):
                if TextBlob(w).tags=='VBZ':
                    wo=Word(w)
                    interm_words.append(wo.lemmatize('v'))
                else:
                    wo=Word(w)
                    interm_words.append(wo.lemmatize())
        words+=interm_words
    return(words)

#print(get_words(file))
