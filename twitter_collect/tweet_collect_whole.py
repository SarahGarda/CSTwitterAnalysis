from credentials import *
from twitter_collect.twitter_connexion_setup import *

def get_candidate_queries(num_candidate):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    name_file='keywords_candidate_'+str(num_candidate)+'.txt'
    try:

        with open(name_file) as file:
            file_reader=file.read().splitlines()
            list=[]
            for row in file_reader:
                list.append(row)
            list.pop(0)
            return(list)
    except IOError:
        raise NameError("the file cannot be read")

#print(get_candidate_queries(1976143068))

