import os
from source.services import UserService


class TestApiTest:

    user_token = ''

    def test_user_login_to_env(self):
        user = {"email": "dmsvtest+postman@gmail.com", "password": "@2663"}
        user_first_name = os.environ['FIRST_NAME']
        user_last_name = os.environ['LAST_NAME']
        user_subscription_date = os.environ['SUBSCRIBE_DATE']
        response = UserService().user_login(user)
        assert response.status_code(200)
        json_data = response.parse_response()
        assert json_data['first_name'] == user_first_name
        assert json_data['last_name'] == user_last_name
        assert json_data['subscriptions']['subscribe_date'] == user_subscription_date
        TestApiTest().user_token = json_data['auth_token']

    def test_get_user_info(self):
        end_point = os.environ['GET_USER_INFO_END_POINT']
        user_email = os.environ['USER_EMAIL']
        field_area = os.environ['FIELD_AREA']
        response = UserService().user_info(end_point, TestApiTest().user_token)
        assert response.status_code(200)
        json_data = response.parse_response()
        assert json_data['email'] == user_email
        assert json_data['area_count'] == field_area


