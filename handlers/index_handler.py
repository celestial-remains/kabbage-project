''' Handler for index page '''

import os
import sys
import jinja2
import json
import webapp2
import urllib
from config import config
from common import TwitterSearch
# Set path to Templates
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),
        '../Templates/')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class IndexHandler(webapp2.RequestHandler):
    ''' Handles landing page requests '''

    def get(self):
        template_values = {
            "site_name": config["site"]["site_name"],
            "site_description": config["site"]["site_description"],
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render(template_values))

    def post(self):
        self.error_message = None
        self.stati = None

        # Process input
        if self.request.body:
            request_body = json.loads(self.request.body)
            if "text" in request_body:
                user_input = request_body["text"]
                if len(user_input) > 0:

                    # Make call to twitter search api with user input
                    try:
                        stats = TwitterSearch.search(user_input)
                        try:
                            if len(stats)>0:
                                self.stati = stats
                            else:
                                self.error_message = \
                                    ["No one seems to care about that topic.."]
                        except Exception as e:
                            self.error_message = \
                                "Twitter is having some technical problems.."
                    except Exception as e:
                        self.error_message = str(e)
                else :
                     self.error_message = "Enter something.."
        # Return results
        data = {
            "error_message": self.error_message,
            "stati": self.stati
        }
        self.response.out.write(json.dumps(data))

