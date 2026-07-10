import pytest

from config import EMAIL, PASSWORD
from services.auth_service import AuthService


@pytest.fixture
def admin_token():
    auth_service = AuthService()

    response = auth_service.login(EMAIL, PASSWORD)

    assert response.status_code == 200

    return response.json()["access_token"]
