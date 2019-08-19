from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
import twitter_credentials
import file_outputter
from dynamo_db_repository import DynamoDBRepository
from twitter_parser import TwitterParser

import json

twitter_accounts = ['@Monzo', '@Get_Chip', '@Revolut', '@StarlingBank']
twitter_count_limit = 100

#  TWITTER CLIENT
class TwitterClient():
    def __init__(self):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
    
    def get_tweets(self, search_terms):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, 
                            q=search_terms, 
                            result_type ='recent', 
                            count = twitter_count_limit,
                            lang='en',
                            wait_on_rate_limit=True).items():
            tweets.append(tweet._json)
        return tweets



#  TWITTER AUTHENTICATOR
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


#  TWITTER STREAMER 
class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, twitter_account):
        listener = TwitterListener(twitter_account)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        stream.filter(track=twitter_account)


#  TWITTER STREAM LISTENER
class TwitterListener(StreamListener):
    
    def __init__(self, twitter_account):
        self.twitter_account = twitter_account

    def on_data(self, data):
        parser = TwitterParser()
        parsedtweets = parser.parse(data,self.twitter_account)
        repository = DynamoDBRepository()
        repository.insert_items(parsedtweets)
    
    def on_error(self, status):
        if status == 420:
            return False
        print(status)


if __name__ == "__main__":

    found_tweets = []
    twitter_client = TwitterClient() 
    parser = TwitterParser()
    repository = DynamoDBRepository()

    for account in twitter_accounts: 
        tweets = twitter_client.get_tweets(account)
        found_tweets.extend(parser.parse(tweets, account))
    
    repository.insert_items(found_tweets)



 




