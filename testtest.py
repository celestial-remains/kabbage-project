
import unittest
import json
from webtest import TestApp
from google.appengine.ext import webapp
from handlers import IndexHandler
from common import TwitterSearch

class IndexTest(unittest.TestCase):

    def setUp(self):
        self.application = webapp.WSGIApplication([('/', IndexHandler)], debug=True)

    def test_get(self):
        app = TestApp(self.application)
        response = app.get('/', json.dumps({ 'text': 'sdfsdf' }))
        self.assertEqual('200 OK', response.status)

    def test_input_post(self):
        app = TestApp(self.application)
        response = app.post('/', json.dumps({ 'text': 'Ronda' }))
        print "Ronda: ", response
        self.assertEqual('200 OK', response.status)

        response = app.post('/', json.dumps({ 'text': 'something'}))
        self.assertEqual('200 OK', response.status)

        response = app.post('/', json.dumps({ 'text': '#help'}))
        print "#help: ", response
        self.assertEqual('200 OK', response.status)

        response = app.post('/', json.dumps({ 'text': '~k'}))
        self.assertEqual('200 OK', response.status)

        response = app.post('/', json.dumps({ 'text': '-j'}))
        self.assertEqual('200 OK', response.status)

        response = app.post('/', json.dumps({ 'text': 'kljdfkjweio23kn3knkbv'}))
        self.assertEqual('200 OK', response.status)
        response = app.post('/', "")

    def test_get_twitter_api(self):
        api = TwitterSearch.get_api()
        self.assertTrue(api is not None)
 
    def test_search_twitter(self):
        print TwitterSearch.search("something")
        print TwitterSearch.search("@")
        print TwitterSearch.search("@james")
        print TwitterSearch.search("#help")
        print TwitterSearch.search("")

if __name__ == '__main__':
    unittest.main()