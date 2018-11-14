def get_tweets_from_candidates_search_queries(queries, twitter_api):
    '''
    :param queries:list of keywords and hashtags
    :param twitter_api: connexion setup to twitter that gives access to the API
    :return: shows the tweets that correspond to the different keywords
    '''
    for keyword in queries:
        tweets = twitter_api.search("keyword",language="french",rpp=100)
        for tweet in tweets:
            print(tweet.text)