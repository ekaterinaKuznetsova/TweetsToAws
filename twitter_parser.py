import json

class TwitterParser():
    def __init__(self):
        pass
    
    def parse_sinlge_tweet(self, tweet, twitter_account):
        tweet_dictionary = {}

        tweet_dictionary['twitter_account']   = twitter_account
        tweet_dictionary['created_at']        = tweet['created_at']
        tweet_dictionary['tweet_id']          = tweet["id"]
        tweet_dictionary['user_id']           = tweet["user"]["id"]
        tweet_dictionary['user_screen_name']  = tweet["user"]["screen_name"]
        tweet_dictionary['text']              = tweet["text"]
        tweet_dictionary['followers_count']   = tweet["user"]["followers_count"]
        tweet_dictionary['retweet_count']     = tweet["retweet_count"]

        hts  =  tweet["entities"]["hashtags"]

        hashtags = ['None']
        if len(hts) != 0 :
            hashtags.pop()
            for ht in hts :
                hashtags.append(str(ht["text"]))
        tweet_dictionary['hashtags'] = hashtags

        return tweet_dictionary

    def parse(self, data, twitter_account): 
        items = []
        for tweet in data: 
            item_dict = self.parse_sinlge_tweet(tweet, twitter_account)
            items.append(item_dict)

        return items


