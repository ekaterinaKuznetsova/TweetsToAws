import json

class FileOutputer():
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, data): 
        try:
            with open(self.file_name, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True

    def save_list(self, data_as_list): 
        for item in data_as_list:
            self.save(item)
        
    def save_json(self, json_data): 
        try:
            with open(self.file_name, 'a') as tf:
                for item in json_data:
                    json.dump(item, tf)
            return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True

# user = User
# autor = User()
# geo=None,
# coordinates=None,
# place=None,
# contributors=None,
# is_quote_status=False,
# retweet_count=0,
# favorite_count=1,
# favorited=False,
# retweeted=False,
# lang='en'
    