from models import User


def test_user_creation():
    user = User(1, "Иван Иванов", "ivan@company.ru")
    assert user.id == 1
    assert user.name == "Иван Иванов"
    assert user.email == "ivan@company.ru"


def test_user_from_data():
    data = {"id": 2, "name": "Анна Смирнова", "email": "anna@company.ru"}
    user = User.from_data(data)
    assert user.id == 2
    assert user.name == "Анна Смирнова"
    assert "anna@company.ru" in str(user)
