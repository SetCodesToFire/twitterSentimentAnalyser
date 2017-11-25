import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key = 'qkoMyfyPqvGtIgJEYLbciFUXz'
consumer_secret = '2S54ZGd7oSv87uGeovhE2nZ9QyHwg5iNvggZRmHrE7H9naaoth'

access_token = '704961007-jM1Iad3nHgnRB5dDqJHwVvrRe1s7WWWttNygiOwH'
access_token_secret = 'ggmLpgBd8ERtzlkFfgZTPp59nMaRSgR0qJRy7ZWo9YgEs'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Padmavati')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)

    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
