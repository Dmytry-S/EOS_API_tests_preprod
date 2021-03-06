import os
import pytest
from source.services import UserService


@pytest.fixture(scope='class', autouse=True)
def user_token():
    email = os.environ['USER_EMAIL']
    password = os.environ['PASSWORD']
    user = {"email": email, "password": password}
    user_subscription_date = os.environ['SUBSCRIBE_DATE']
    response = UserService().user_login(user)
    assert response.status_code(200)
    json_data = response.parse_response()
    assert json_data['subscriptions']['subscribe_date'] == user_subscription_date
    user_token = json_data['auth_token']
    return user_token
