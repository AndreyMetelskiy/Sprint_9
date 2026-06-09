import uuid

BASE_URL = "https://foodgram-frontend-1.foodgram.education-services.ru"

RECIPE = {
    "name": "Тестовый рецепт",
    "ingredient": "абрикос",
    "ingredient_amount": "100",
    "cooking_time": "10",
}

def get_unique_user():
    unique = uuid.uuid4().hex[:8]
    return {
        "email": f"user_{unique}@test.ru",
        "username": f"user_{unique}",
        "first_name": "Тест",
        "last_name": "Пользователь",
        "password": "Selenium2024x",
    }
