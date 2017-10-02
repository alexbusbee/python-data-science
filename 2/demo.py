import tweepy
from textblob import TextBlob

consumer_key = 'KoQL2MYFeSBC8nbgz1tcIc7Ci'
consumer_secret = 'bRvp7l2jxg68kgLDqV2RKia3AHn0AOONZkU9egcmgvBbKv3ltG'

access_token = '365127594-3CYFvf6CJWrguDdemKn1mYp8A6yiQeYFKe3ruuxn'
access_token_secret = 'PEQ5cFfDO882SRl9PZpgW8mfFfPAKjOgYrdkltSXmBVbB'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)