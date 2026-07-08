from faker import Faker
import allure
import pytest
from services.users_service import UsersService
from models.user_model import UserModel


faker = Faker()


@allure.feature("Users API")
@allure.title("Получение списка пользователей")
def test_get_users(admin_token):
    users_service = UsersService()
    with allure.step("Получить список пользователей"):
        response = users_service.get_users(admin_token)
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200
    with allure.step("Проверить модель пользователя"):
        UserModel(**response.json()[0])


@allure.feature("Users API")
@allure.title("Обновление пользователя")
def test_update_user(admin_token):
    users_service = UsersService()
    with allure.step("Получить id пользователя"):
        user_id = users_service.get_users(admin_token).json()[0]["id"]
    with allure.step("Подготовить новые данные пользователя"):
        user_data = {
            "username": faker.user_name(),
            "email": faker.email(),
            "role": "user",
            "avatar_url": None,
        }
    with allure.step("Обновить пользователя"):
        response = users_service.update_user(user_id, user_data, admin_token)
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200
    with allure.step("Проверить модель и обновленные данные"):
        UserModel(**response.json())
        assert response.json()["username"] == user_data["username"]
        assert response.json()["email"] == user_data["email"]


@allure.feature("Users API")
@allure.title("Удаление пользователя")
def test_delete_user(admin_token):
    users_service = UsersService()
    with allure.step("Получить id пользователя"):
        user_id = users_service.get_users(admin_token).json()[0]["id"]
    with allure.step("Удалить пользователя"):
        response = users_service.delete_user(user_id, admin_token)
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 204


@allure.feature("Users API")
@allure.title("Получение пользователей с параметрами")
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
    with allure.step(f"Получить пользователей skip={skip}, limit={limit}"):
        response = users_service.get_users(admin_token, skip=skip, limit=limit)
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200
    with allure.step("Проверить модель пользователя"):
        users = response.json()
    if users:
        UserModel(**users[0])


@allure.feature("Users API")
@allure.title("Получение пользователей без токена")
def test_get_users_without_token():
    users_service = UsersService()
    with allure.step("Отправить запрос без токена"):
        response = users_service.get_users("")
    with allure.step("Проверить ошибку авторизации"):
        assert response.status_code == 401


@allure.feature("Users API")
@allure.title("Обновление пользователя с некорректным email")
def test_update_user_with_invalid_email(admin_token):
    users_service = UsersService()
    with allure.step("Получить id пользователя"):
        user_id = users_service.get_users(admin_token).json()[0]["id"]
    with allure.step("Подготовить данные с некорректным email"):
        user_data = {
            "username": faker.user_name(),
            "email": "invalid_email",
            "role": "user",
            "avatar_url": None,
        }
    with allure.step("Отправить запрос на обновление пользователя"):
        response = users_service.update_user(
            user_id=user_id, user_data=user_data, token=admin_token)
    with allure.step("Проверить ошибку валидации"):
        assert response.status_code == 422


@allure.feature("Users API")
@allure.title("Обновление пользователя с пустым username")
def test_update_user_with_empty_username(admin_token):
    users_service = UsersService()
    with allure.step("Получить id пользователя"):
        user_id = users_service.get_users(admin_token).json()[0]["id"]
    with allure.step("Подготовить данные с пустым username"):
        user_data = {
            "username": "",
            "email": faker.email(),
            "role": "user",
            "avatar_url": None,
        }
    with allure.step("Отправить запрос на обновление пользователя"):
        response = users_service.update_user(
            user_id=user_id, user_data=user_data, token=admin_token)
    with allure.step("Проверить ошибку валидации"):
        assert response.status_code == 422


@allure.feature("Users API")
@allure.title("Обновление пользователя с пустым email")
def test_update_user_with_empty_email(admin_token):
    users_service = UsersService()
    with allure.step("Получить id пользователя"):
        user_id = users_service.get_users(admin_token).json()[0]["id"]
    with allure.step("Подготовить данные с пустым email"):
        user_data = {
            "username": faker.user_name(),
            "email": "",
            "role": "user",
            "avatar_url": None,
        }
    with allure.step("Отправить запрос на обновление пользователя"):
        response = users_service.update_user(
            user_id=user_id, user_data=user_data, token=admin_token)
    with allure.step("Проверить ошибку валидации"):
        assert response.status_code == 422


@allure.feature("Users API")
@allure.title("Проверка валидации поля role")
def test_update_user_with_invalid_role(admin_token):
    users_service = UsersService()
    with allure.step("Получить id пользователя"):
        user_id = users_service.get_users(admin_token).json()[0]["id"]
    with allure.step("Подготовить данные с некорректной role"):
        user_data = {
            "username": faker.user_name(),
            "email": faker.email(),
            "role": "superuser",
            "avatar_url": None,
        }
    with allure.step("Отправить запрос на обновление пользователя"):
        response = users_service.update_user(
            user_id=user_id, user_data=user_data, token=admin_token)
    with allure.step("Проверить ошибку валидации"):
        assert response.status_code == 422


@allure.feature("Users API")
@allure.title("Получение пользователей без результата")
def test_get_users_not_found(admin_token):
    users_service = UsersService()
    with allure.step("Получить пользователей за пределами списка"):
        response = users_service.get_users(
            admin_token,
            skip=1000,
            limit=10,
        )
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200
    with allure.step("Проверить пустой список"):
        assert response.json() == []
