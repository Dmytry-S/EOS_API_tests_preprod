import json


class AssertResponse(object):

    def __init__(self, response):
        self.response = response

    def status_code(self, code):
        return self.response.status_code == code

    def parse_response(self):
        return self.response.json()
