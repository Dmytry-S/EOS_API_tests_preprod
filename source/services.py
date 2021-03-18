import json
import os
import requests
from source.response import AssertResponse


class ApiTestService(object):

    def __init__(self):
        self.login_url = os.environ['LOGIN_URL']
        self.base_url = os.environ['BASE_URL']

    def post(self, body, end_point=''):
        return requests.post(f"{self.login_url}", data=json.dumps(body), headers={'content-type': 'application/json'})

    def get(self, end_point, user_token):
        return requests.get(f"{self.base_url} + {end_point}",
                            headers={'content-type': 'application/json',
                                     'Authorization': 'Token {}'.format(user_token)})

    def delete(self):
        pass


class UserService(ApiTestService):

    def __init__(self):
        super().__init__()

    def user_login(self, user):
        return AssertResponse(self.post(user))

    def user_info(self, end_point, token):
        return AssertResponse(self.get(end_point, token))

