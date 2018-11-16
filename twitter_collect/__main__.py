from twitter_collect.tweet_candidate_actuality_tweets import *
from twitter_collect.tweet_collect_whole import *
from twitter_collect.tweet_candidate_tweet_activity import *
from twitter_collect.twitter_connexion_setup import *
import time

def collection(num_candidate,time_limit):
    '''
    :param num_candidate: the user_id of the candidate's Twitter account, type=int
    :param time_lmit: in seconds, the time for which the streaming runs, type=int
    :param file_path: the path to the keyword and hashtag files
    :return: return the relevant tweets about a candidate
    '''
    whole=[]
    print('recent tweets')
    for querie in get_candidate_queries(num_candidate):
        print(get_tweets_from_candidates_search_queries(querie, twitter_setup()))
    whole.append(get_candidate_queries(num_candidate))
    print('replies')
    print(get_replies_to_candidates(num_candidate))
    whole.append(get_replies_to_candidates(num_candidate))
    print('retweets')
    print(get_retweets_of_candidates(num_candidate))
    whole.append(get_retweets_of_candidates(num_candidate))
    print('streaming tweets')
    streaming=[]
    start_time=time.time()
    if (time.time()-start_time)<time_limit:
        print(candidate_activity_streaming(num_candidate))
        streaming.append(candidate_activity_streaming(num_candidate))
    whole.append(streaming)
    return(whole)



#collection(1976143068,10)
