import os

from source.services import UserService


class TestApiTest:

    def test_get_user_info(self, user_token):
        end_point = os.environ['GET_USER_INFO_END_POINT']
        user_email = os.environ['USER_EMAIL']
        field_area = os.environ['FIELD_AREA']
        measurement_system = os.environ['MEASUREMENT_SYSTEM']
        country_iso = os.environ['COUNTRY_ISO']
        response = UserService().user_param(end_point, user_token)
        assert response.status_code(200)
        json_data = response.parse_response()
        assert json_data['email'] == user_email
        assert json_data['area_count'] == float(field_area)
        assert json_data['measurement_system'] == measurement_system
        assert json_data['country_iso'] == country_iso

    def test_user_subscription(self, user_token):
        end_point = os.environ['USER_SUBSCRIPTION_END_POINT']
        subscription_start = os.environ['SUBSCRIPTION_START']
        subscription_finish = os.environ['SUBSCRIPTION_FINISH']
        subscription_name = os.environ['SUBSCRIPTION_NAME']
        subscription_type = os.environ['SUBSCRIPTION_TYPE']
        pro_fields_area = os.environ['PRO_FIELDS_AREA']
        enable_worklog = os.environ['ENABLE_WORKLOG']
        enable_splitview = os.environ['ENABLE_SPLITVIEW']
        response = UserService().user_param(end_point, user_token)
        assert response.status_code(200)
        json_data = response.parse_response()
        assert json_data['subscription']['date_start'] == subscription_start
        assert json_data['subscription']['date_finish'] == subscription_finish
        assert json_data['subscription']['name'] == subscription_name
        assert json_data['subscription']['type'] == subscription_type
        assert json_data['subscription']['active']
        assert json_data['restrictions']['pro_fields_area'] == int(pro_fields_area)
        assert json_data['subscription']['enable_worklog'] == enable_worklog
        assert json_data['subscription']['enable_splitview'] == enable_splitview
        assert json_data['restrictions']['satellite_images_view']
        assert json_data['restrictions']['weather_data']
        assert json_data['restrictions']['zoning']

    def test_data_manager_mb_before_upload(self, user_token):
        end_point = os.environ['DATA_MB_RESTRICTION_END_POINT']
        total_available_mb = os.environ['TOTAL_AVAILABLE_MB']
        total_uploaded_mb = os.environ['TOTAL_UPLOADED_MB']
        response = UserService().user_param(end_point, user_token)
        assert response.status_code(200)
        json_data = response.parse_response()
        assert json_data['total_available_mb'] == float(total_available_mb)
        assert json_data['total_uploaded_mb'] == float(total_uploaded_mb)

    def test_upload_file(self, user_token):
        end_point = os.environ['UPLOAD_FILE_END_POINT']
        upload_status = os.environ['UPLOAD_STATUS']
        upload_area = os.environ['UPLOAD_AREA']
        upload_size = os.environ['UPLOAD_SIZE']
        response = UserService().upload_file(end_point, user_token)
        assert response.status_code(201)
        json_data = response.parse_response()
        assert json_data['status'] == upload_status
        assert json_data['area'] == float(upload_area)
        assert json_data['size'] == float(upload_size)

    def test_data_manager_mb_after_upload(self, user_token):
        end_point = os.environ['DATA_MB_RESTRICTION_END_POINT']
        total_available_mb = os.environ['TOTAL_AVAILABLE_MB']
        total_uploaded_mb = os.environ['TOTAL_UPLOADED_MB_WITH_DATA']
        response = UserService().user_param(end_point, user_token)
        assert response.status_code(200)
        json_data = response.parse_response()
        assert json_data['total_available_mb'] == float(total_available_mb)
        assert json_data['total_uploaded_mb'] == float(total_uploaded_mb)

    def test_delete_file(self, user_token):
        end_point = os.environ['DELETE_FILE_END_POINT']
        response = UserService().delete_file(end_point, user_token)
        assert response.status_code(204)

    def test_data_manager_mb_after_delete(self, user_token):
        end_point = os.environ['DATA_MB_RESTRICTION_END_POINT']
        total_available_mb = os.environ['TOTAL_AVAILABLE_MB']
        total_uploaded_mb = os.environ['TOTAL_UPLOADED_MB']
        response = UserService().user_param(end_point, user_token)
        assert response.status_code(200)
        json_data = response.parse_response()
        assert json_data['total_available_mb'] == float(total_available_mb)
        assert json_data['total_uploaded_mb'] == float(total_uploaded_mb)

    def test_data_manager_demo_data(self, user_token):
        end_point = os.environ['DEMO_DATA_END_POINT']
        data_name_elevation = os.environ['DATA_NAME_ELEVATION']
        data_name_value = os.environ['DATA_NAME_VALUE']
        response = UserService().user_param(end_point, user_token)
        assert response.status_code(200)
        json_data = response.parse_response()
        assert json_data[0]['name'] == data_name_elevation
        assert json_data[0]['is_active']
        assert json_data[1]['name'] == data_name_value
        assert json_data[1]['is_active']

    def test_field_activity_types(self, user_token):
        end_point = os.environ['FIELD_ACTIVITY_TYPES_END_POINT']
        activity_type_fertilization = os.environ['ACTIVITY_TYPE_FERTILIZATION']
        activity_type_tillage = os.environ['ACTIVITY_TYPE_TILLAGE']
        activity_type_planting = os.environ['ACTIVITY_TYPE_PLANTING']
        activity_type_spraying = os.environ['ACTIVITY_TYPE_SPRAYING']
        activity_type_harvesting = os.environ['ACTIVITY_TYPE_HARVESTING']
        activity_type_default = os.environ['ACTIVITY_TYPE_DEFAULT']
        response = UserService().worklog_data(end_point, user_token)
        assert response.status_code(200)
        json_data = response.parse_response()
        assert json_data[0]['name_en'] == activity_type_fertilization
        assert json_data[1]['name_en'] == activity_type_tillage
        assert json_data[2]['name_en'] == activity_type_planting
        assert json_data[3]['name_en'] == activity_type_spraying
        assert json_data[4]['name_en'] == activity_type_harvesting
        assert json_data[5]['name_en'] == activity_type_default

    def test_crop_types_2021(self, user_token):
        end_point = os.environ['USER_CROP_TYPE_END_POINT']
        id_winter_wheat = os.environ['ID_WINTER_WHEAT']
        name_en_winter_wheat = os.environ['NAME_EN_WINTER_WHEAT']
        id_paprika = os.environ['ID_PAPRIKA']
        name_uk_paprika = os.environ['NAME_UK_PAPRIKA']
        id_wheat = os.environ['ID_WHEAT']
        name_ru_wheat = os.environ['NAME_RU_WHEAT']
        id_buckwheat = os.environ['ID_BUCKWHEAT']
        name_pt_buckwheat = os.environ['NAME_PT_BUCKWHEAT']
        id_corn = os.environ['ID_CORN']
        name_es_corn = os.environ['NAME_ES_CORN']
        parameters = {'year': '2021'}
        response = UserService().worklog_data(end_point, user_token, parameters)
        assert response.status_code(200)
        json_data = response.parse_response()
        assert json_data[0]['id'] == int(id_winter_wheat)
        assert json_data[0]['name_en'] == name_en_winter_wheat
        assert json_data[1]['id'] == int(id_paprika)
        assert json_data[1]['name_uk'] == name_uk_paprika
        assert json_data[2]['id'] == int(id_wheat)
        assert json_data[2]['name_ru'] == name_ru_wheat
        assert json_data[3]['id'] == int(id_buckwheat)
        assert json_data[3]['name_pt'] == name_pt_buckwheat
        assert json_data[4]['id'] == int(id_corn)
        assert json_data[4]['name_es'] == name_es_corn

    def test_field_activities_2021(self, user_token):
        end_point = os.environ['FIELD_ACTIVITY_TYPES_END_POINT']
        activity_fertilization = os.environ['ACTIVITY_TYPE_FERTILIZATION']
        activity_spraying = os.environ['ACTIVITY_TYPE_SPRAYING']
        activity_harvesting = os.environ['ACTIVITY_TYPE_HARVESTING']
        parameters = {'year': '2021'}
        response = UserService().worklog_data(end_point, user_token, parameters)
        assert response.status_code(200)
        json_data = response.parse_response()
        assert len(json_data) == 3
        assert json_data[0]['name_en'] == activity_fertilization
        assert json_data[1]['name_en'] == activity_spraying
        assert json_data[2]['name_en'] == activity_harvesting











