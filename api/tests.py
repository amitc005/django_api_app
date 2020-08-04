import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestTodoAPI:
    @pytest.fixture(autouse=True)
    def setUp(self):
        login_data = {"username": "testuser", "password": "abc123"}
        user = User.objects.create_user(**login_data)
        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def test_get_todo_list(self):
        data = {"title": "Creating test", "body": "Creating test todo body"}
        response = self.client.post("/api/todos/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/todos/")
        assert response.status_code == 200
        assert len(response.json()) == 1
        res_data = response.json()[0]
        assert "id" in res_data and res_data["id"] == 1
        del res_data["id"]
        assert res_data == data
