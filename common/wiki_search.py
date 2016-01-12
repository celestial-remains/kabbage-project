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
            search_results = wikipedia.search(user_input)
            wiki_results = []
            for result in search_results:
                try:
                    page = wikipedia.page(result)
                    wiki_results.append({"title": page.title, "url": page.url})
                except wikipedia.exceptions.WikipediaException as e:
                    pass
            return wiki_results
        except Exception as e:
            return None
