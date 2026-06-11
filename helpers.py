import uuid

from test_data import UserData


def get_unique_user():
    unique = uuid.uuid4().hex[:8]
    return {
        "email": f"user_{unique}@test.ru",
        "username": f"user_{unique}",
        "first_name": UserData.FIRST_NAME,
        "last_name": UserData.LAST_NAME,
        "password": UserData.PASSWORD,
    }
