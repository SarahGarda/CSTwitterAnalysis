from tweet_analysis.analysis import *
from tweet_text2.sentiment_analysis import *
import seaborn as sns
import matplotlib.pyplot as plt

def tweet_polarity():
    '''
    :return: the graphs of the percentage of positive, negative and neutral tweets
    '''
    sns.set(style="white", context="talk")
    f, (ax1) = plt.subplots(1, 1, figsize=(7, 5), sharex=True)
    y=sentiment_percentage(file)
    x=['Positive tweets', 'Neutral tweets', 'Negative tweets']
    sns.barplot(x=x, y=y, palette="rocket", ax=ax1)
    ax1.axhline(0, color="k", clip_on=False)
    ax1.set_ylabel("Percentage")
    sns.despine(bottom=True)
    plt.setp(f.axes, yticks=[])
    plt.tight_layout(h_pad=2)
    plt.show()


print(interest_graph())
#interest_graph has been written before in tweet_analysis.analysis
print(tweer_polarity)
