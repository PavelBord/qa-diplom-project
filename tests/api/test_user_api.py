from faker import Faker
import pytest
from services.users_service import UsersService
from models.user_model import UserModel


faker = Faker()


def test_get_users(admin_token):
    users_service = UsersService()

    response = users_service.get_users(admin_token)

    assert response.status_code == 200

    UserModel(**response.json()[0])


def test_update_user(admin_token):
    users_service = UsersService()

    user_id = users_service.get_users(admin_token).json()[0]["id"]

    user_data = {
        "username": faker.user_name(),
        "email": faker.email(),
        "role": "user",
        "avatar_url": None,
    }

    response = users_service.update_user(user_id, user_data, admin_token)

    assert response.status_code == 200

    UserModel(**response.json())
    assert response.json()["username"] == user_data["username"]
    assert response.json()["email"] == user_data["email"]


def test_delete_user(admin_token):
    users_service = UsersService()

    user_id = users_service.get_users(admin_token).json()[0]["id"]

    response = users_service.delete_user(user_id, admin_token)

    assert response.status_code == 204


@pytest.mark.parametrize(
    "skip, limit",
    [
        (0, 1),
        (0, 10),
        (1, 5),
        (100, 1),
    ],
)
def test_get_users_with_params(admin_token, skip, limit):
    users_service = UsersService()

    response = users_service.get_users(admin_token, skip=skip, limit=limit)

    assert response.status_code == 200

    users = response.json()
    if users:
        UserModel(**users[0])


def test_get_users_without_token():
    users_service = UsersService()

    response = users_service.get_users("")

    assert response.status_code == 401


def test_update_user_with_invalid_email(admin_token):
    users_service = UsersService()
    user_id = users_service.get_users(admin_token).json()[0]["id"]
    user_data = {
        "username": faker.user_name(),
        "email": "invalid_email",
        "role": "user",
        "avatar_url": None,
    }
    response = users_service.update_user(
        user_id=user_id, user_data=user_data, token=admin_token)

    assert response.status_code == 422


def test_update_user_with_empty_username(admin_token):
    users_service = UsersService()
    user_id = users_service.get_users(admin_token).json()[0]["id"]
    user_data = {
        "username": "",
        "email": faker.email(),
        "role": "user",
        "avatar_url": None,
    }
    response = users_service.update_user(
        user_id=user_id, user_data=user_data, token=admin_token)

    assert response.status_code == 422


def test_update_user_with_empty_email(admin_token):
    users_service = UsersService()

    user_id = users_service.get_users(admin_token).json()[0]["id"]

    user_data = {
        "username": faker.user_name(),
        "email": "",
        "role": "user",
        "avatar_url": None,
    }

    response = users_service.update_user(
        user_id=user_id, user_data=user_data, token=admin_token)

    assert response.status_code == 422


def test_update_user_with_invalid_role(admin_token):
    users_service = UsersService()

    user_id = users_service.get_users(admin_token).json()[0]["id"]

    user_data = {
        "username": faker.user_name(),
        "email": faker.email(),
        "role": "superuser",
        "avatar_url": None,
    }

    response = users_service.update_user(
        user_id=user_id, user_data=user_data, token=admin_token)

    assert response.status_code == 422


def test_get_users_not_found(admin_token):
    users_service = UsersService()

    response = users_service.get_users(
        admin_token,
        skip=1000,
        limit=10,
    )

    assert response.status_code == 200
    assert response.json() == []
