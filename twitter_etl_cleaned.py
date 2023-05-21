import tweepy 
import pandas as pd
import json
from datetime import datetime
import s3fs


def run_twitter_etl():

        #Twitter Authentication
        auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
         )

        api = tweepy.API(auth)

        tweets = api.user_timeline(screen_name = '@narendramodi',
                                   count=50,
                                   include_rts = False,
                                   tweet_mode = 'extended'
                                   )
        tweet_list = []
        for tweet in tweets:
                #print(tweet)
                text = tweet._json["full_text"]

        #data cleaning
                transformed_tweet = {
                              "user": tweet.user.screen_name,
                              'text' : text,
                              'favorite_count' : tweet.favorite_count,
                              'retweet_count' : tweet.retweet_count,
                              'created_at' : tweet.created_at
                  
                            }
                tweet_list.append(transformed_tweet)

        df = pd.DataFrame(tweet_list)
        df.to_csv('s3://<folder>/pm_modi_tweets.csv')


#run_twitter_etl()
