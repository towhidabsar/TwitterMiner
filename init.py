import tweepy
import json
import config

auth = tweepy.OAuthHandler(	config.app_key, config.app_secret)
auth.set_access_token(config.access_token, config.token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet


class MarketviewHeightsListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_data(self, raw_data):
        tweets = json.loads(raw_data)
        print tweets['text']
        with open("dataset.txt","a") as tf:
            tf.write(raw_data)
        return True

    def on_error(self, status_code):
        print status_code
        if status_code == 420:
            return False

marketViewListener = MarketviewHeightsListener()
tweetStream = tweepy.Stream(auth= api.auth, listener=marketViewListener)
#tweetStream.filter(track=['python'])
tweetStream.filter(locations=[-77.604706, 43.162895,-77.593314, 43.169461])

#NorthEast 43.169461, -77.593314
#NorthWest  43.162895, -77.604706