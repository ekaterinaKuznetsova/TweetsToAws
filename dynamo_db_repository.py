import boto3 
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.client('dynamodb')


class DynamoDBRepository():
    
    def insert_item(self, data):
        dynamodb.put_item(
            TableName  = 'TwitterTweets',
            Item={
                'twitter_account'  :  {"S" : str(data['twitter_account'])},
                'created_at'       :  {"S" : str(data['created_at'])},
                'tweet_id'         :  {"S" : str(data['tweet_id'])},
                'user_id'          :  {"S" : str(data['user_id'])},
                'user_screen_name' :  {"S" : str(data['user_screen_name'])},
                'text'             :  {"S" : str(data['text'])},
                'hashtags'         :  {"SS": data['hashtags']},
                'followers_count'  :  {"S" : str(data['followers_count'])},
                'retweet_count'    :  {"S" : str(data['retweet_count'])}
                
            }
        )

    def insert_items(self, data): 
        for item in data:
            self.insert_item(item)

    # def get_max_id(self, dynamodb_table ):
    #     table = dynamodb.Table(dynamodb_table)
    #     tweet_id = str(1162740239716233217)
    #     max_id = list(table.query(ScanIndexForward=False, Limit=1, KeyConditionExpression=Key('tweet_id').eq(tweet_id) & Key('created_at').lte('2019-01-01')))
    #     return max_id
    #     # ['created_at']
    


