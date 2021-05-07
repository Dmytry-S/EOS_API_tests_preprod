import json
import os
import requests
from source.response import AssertResponse
# import allure


class ApiTestService(object):

    def __init__(self):
        self.login_url = os.environ['LOGIN_URL']
        self.base_url = os.environ['BASE_URL']

    def post(self, body, end_point=''):
        return requests.post(self.login_url, data=json.dumps(body), headers={'content-type': 'application/json'})

    def get(self, end_point, user_token):
        return requests.get(self.base_url + end_point,
                            headers={'Authorization': 'Token {}'.format(user_token)})

    def post_upload(self, end_point, user_token):
        files = {'data': ('movchanovka.zip', open('movchanovka.zip', 'rb'), 'multipart/form-data')}
        return requests.post(self.base_url + end_point, files=files,
                             headers={'Authorization': 'Token {}'.format(user_token)})

    def delete(self, end_point, user_token):
        return requests.delete(self.base_url + end_point,
                               headers={'Authorization': 'Token {}'.format(user_token)})

    def get_worklog(self, end_point, user_token, parameters={}):
        x_team_id = os.environ['X_TEAM_ID']
        return requests.get(self.base_url + end_point, params=parameters,
                            headers={'Authorization': 'Token {}'.format(user_token),
                                     'x-team-id': x_team_id})


class UserService(ApiTestService):

    def __init__(self):
        super().__init__()

    # @allure.step
    def user_login(self, user):
        return AssertResponse(self.post(user))

    # @allure.step
    def user_param(self, end_point, token):
        return AssertResponse(self.get(end_point, token))

    # @allure.step
    def upload_file(self, end_point, token):
        return AssertResponse(self.post_upload(end_point, token))

    # @allure.step
    def delete_file(self, end_point, token):
        return AssertResponse(self.delete(end_point, token))

    # @allure.step
    def worklog_data(self, end_point, token, parameters={}):
        return AssertResponse(self.get_worklog(end_point, token, parameters))
