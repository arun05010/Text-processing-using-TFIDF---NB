import tweepy

# Twitter Authentication keys
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

# Passing the unique keys, tokens, etc.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) auth.set_access_token(access_token, access_token_secret)

# Establishing connection
api = tweepy.API(auth)

# Retrieve Tweets.
public_tweets = api.search('data')

# Printing the tweets.
for tweet in public_tweets: print(tweet.text) print("")
