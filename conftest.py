# import pytest
# from django.contrib.auth.models import User
# from rest_framework.test import APIClient


# @pytest.fixture(scope="session")
# def token(django_db_setup, django_db_blocker):
#     login_data = {"username": "testuser", "password": "abc123"}
#     with django_db_blocker.unblock():
#         testuser1 = User.objects.create_user(**login_data)
#         testuser1.save()
#         response = APIClient().post("/api/auth/login/", data=login_data)
#         assert response.status_code == 200
#         assert "key" in response.json()
#         return response.json()["key"]
