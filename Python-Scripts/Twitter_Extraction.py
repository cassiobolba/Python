import tweepy as tw
import pandas as pd
import datetime as dt
import fastparquet 
from log_module import logger_error,logger_info

consumer_key = 'your key'
consumer_secret = 'your key'
access_token = ' your key'
access_token_secret = 'your key'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

# Define the search term 
search_words = "#yourhashtag"

# Define the date range to look for the search_word
# if both are set to 0 = current day
# past 7 days up to yesterday = start_days = 7 and end_days = -1
start_days = 0
end_days = 0
today = dt.date.today()

date_since = today - dt.timedelta(days=start_days)
date_until = today + dt.timedelta(days=end_days)

# Connecting with API to do a search based on date and query
try:
    tweets = tw.Cursor(api.search 
                            ,q = search_words
                            ,since = date_since
                            ,until = date_until
                        ).items(1000)

    users_locs = [[ 
                     tweet.id
                    ,tweet.user.id
                    ,tweet.user.location
                    ,tweet.user.followers_count
                    ,tweet.created_at
                    ,tweet.text 
                    ,tweet.user.statuses_count
                    ]for tweet in tweets]
    logger_info(f"Hashtag search was sucessfull from {date_since} to {date_until} !",today)
except Exception as e:
    logger_error(e,today)

# Creating parquet file and storing in the raw zone
try:
    if users_locs:
        df = pd.DataFrame(users_locs,columns=[
                                                'tweetId'
                                                ,'userId'
                                                ,'location'
                                                ,'userFollowers'
                                                ,'createdAt'
                                                ,'tweetText'
                                                ,'userTweets'])
        df.to_parquet(f'rawZone/flixBus#{today}.parquet.gzip', compression='gzip')
        logger_info(f"Hashtag search generated file flixBus#{today} from {date_since} to {date_until} !",today)
    else:
        logger_info(f"Hashtag search generated no data from {date_since} to {date_until} !",today)
except Exception as e:
    logger_error(e,today)
    
