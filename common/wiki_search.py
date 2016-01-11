'''' Handy Methods for searching Wikipedia'''

import os
import sys
import urllib

# Fix path to library
sys.path.append(os.path.join(os.path.dirname(__file__), '../lib'))
import wikipedia
from config import config


class WikiSearch():

    @classmethod
    def search(cls,user_input):
        try:
            return wikipedia.search(user_input)
        except Exception as e:
            return e
