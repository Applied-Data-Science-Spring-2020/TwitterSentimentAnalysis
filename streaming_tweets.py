import tweepy
import datetime
import csv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#import import_ipynb
import credentials

keywords = ['Debatenight', 'DemDebate', 'Democrats2020', 'bernie sanders']
filename = 'C:\\Users\\abhin\\Downloads\\twitter_tweets.json'
date_since = "2019-01-10"
flag = False

class stdOutListener(StreamListener):
    
    def __init__(self, filename):
        self.filename = filename
    
    def on_data(self, data):
        try:
            print(data)
            with open(filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on the data %s", str(e))
        return True
    
class twitterStreamer():
    
    def streamTweets(self, filename, keywords):
        listener = stdOutListener(filename)
        auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
        auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
        print("Connection has been established successfully")
        stream = Stream(auth, listener)
        stream.filter(track=keywords)
        while not flag:
            for tweets in stream:
                if datetime.date(2019, 1, 1) < tweet.created_at:
                    flag = True
                    break
            

if __name__ == "__main__":
    tweets = twitterStreamer()
    tweets.streamTweets(filename, keywords)