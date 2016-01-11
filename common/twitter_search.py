'''' Handy Methods for searching Twitter'''

import os
import sys
import urllib

# Fix path to library
sys.path.append(os.path.join(os.path.dirname(__file__), '../lib'))
import twitter

from config import config

class TwitterSearch():

    @classmethod
    def search(cls,user_input):
        try:
            api = cls.get_api()
            search_query = urllib.urlencode({"term": user_input})
            stati = api.GetSearch(search_query)
            statuses = []
            for stat in stati:
                statuses.append(stat.text)
            return statuses
        except Exception as e:
            return e

    @classmethod
    def get_api(cls):
        # Establish connection with twitter api
        consumer_key = config["twitter"]["api_key"]
        consumer_secret = config["twitter"]["api_secret"]
        access_token_key = config["twitter"]["access_token_key"]
        access_token_secret = config["twitter"]["access_token_secret"]
        try:
            api = twitter.Api(consumer_key, consumer_secret, access_token_key,
                access_token_secret, cache=None)
            return api
        except Exception as e:
            return None