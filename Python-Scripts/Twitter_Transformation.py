import pandas as pd
import datetime as dt
import re
import hashlib
import os
from log_module import logger_error,logger_info

# Define the date range to process
days_ago_range = 0
today = dt.date.today()

# Define the date range to look for files to process
# if both are set to 0 = current day
# past 7 days up to yesterday = start_days = 7 and end_days = -1
try:
    files = []
    for i in range(0,days_ago_range+1):
        date = today - dt.timedelta(days=i)
        files.append(f'flixBus#{date}.parquet.gzip')
except Exception as e:
    logger_error('Error Creating list of files to process\n'+str(e),today)

# Looping over the list of files user wants to process
# versus the list os files actually available
try:
    df = pd.DataFrame()
    for i in files:
        if i in os.listdir('c:/Users/cassi/Desktop/Tweeter_Case/rawZone/'):
            new = pd.read_parquet('c:/Users/cassi/Desktop/Tweeter_Case/rawZone/'+i)
            df = df.append(new)
            logger_info(f"File {i} loaded to process!",today)
        else:
            logger_info(f"File {i} was not available to process!",today)
            pass
except Exception as e:
        logger_error('Error Creating list of files to process\n'+str(e),today)

try:
    # Hashing the column UserId, but keeping it traceable
    count_row = df.shape[0]
    for i in range (0, count_row):
        idEncoded = str(df['userId'][i]).encode("utf-8")
        encoded_message = hashlib.md5(idEncoded)
        df['userId'][i] = encoded_message.digest()

    # Creating column with a list of hashtags in the tweet
    df['hashtags'] = ''
    for i in range (0, count_row):
        df['hashtags'][i]  = re.findall(r"#(\w+)",  df['tweetText'][i])

    # Creating column for retweets
    df['isRetweet'] = ''
    for i in range (0, count_row):
        if df['tweetText'][i].startswith("RT @") == True:
            df['isRetweet'][i] = True
        else:
            df['isRetweet'][i] = False

    mapping = {
        'rome' : 'Rome, Italy'
        ,'Roma' : 'Rome, Italy'
        ,'Dolnośląskie, Polska' : 'Dolnośląskie, Poland'
        ,'Małopolskie, Polska' : 'Małopolskie, Poland'	
        ,'Italia' : 'Italy'
        ,'Region Hannover' : 'Hannover, Germany'
        ,'Hamburg (zztl Potsdam/ Berlin)' : 'Hamburg, Germany'
    }

    # Applying a mapping in the location column to standarize names
    for i in range (0, count_row):
        if df['location'][i] in mapping.keys():
            df['location'][i] = mapping[df['location'][i]]

    # Creating a new dataframe to explode each hashtag related to a twitter
    dfHashtags = df[['tweetId','hashtags']]
    dfHashtags = dfHashtags.explode('hashtags')

    # Dopping unecessary columns from df
    df = df.drop(columns=['tweetText','hashtags'])

    # writting to csv files
    df.to_csv(f'c:/Users/cassi/Desktop/Tweeter_Case/consumerZone/FlixbusData/flixBusData_{today}.csv'
            , encoding = 'utf-8-sig')
    dfHashtags.to_csv(f'c:/Users/cassi/Desktop/Tweeter_Case/consumerZone/Hashtags/flixBusHastags_{today}.csv'
            , encoding = 'utf-8')

    logger_info(f"Files loaded were sucessfully processed!",today)
except Exception as e:
    logger_error('Files loaded were not processed today \n'+str(e),today)