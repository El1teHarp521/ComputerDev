from models import Category, State, User, Device


def test_device_creation():
    cat = Category(1, "ПК")
    st = State(1, "Свободно", True)
    dev = Device(1, "Рабочая станция", 999, cat, st)
    assert dev.id == 1
    assert dev.is_available() is True
    assert dev.is_assigned is False


def test_device_interaction():
    cat = Category(1, "Ноутбуки")
    st_free = State(1, "Свободно", True)
    st_busy = State(2, "Выдано", False)
    dev = Device(1, "MacBook Pro", 1001, cat, st_free)
    user = User(1, "Анна", "anna@test.ru")

    # 1. Валидация
    assert Device.validate_inv_number(1001) is True
    assert Device.validate_inv_number(-5) is False

    # 2. Выдача сотруднику
    dev.assign_to_user(user, st_busy)
    assert dev.is_assigned is True
    assert dev.is_available() is False
    assert dev.user is user
    assert dev.state is st_busy

    # 3. Возврат на склад
    dev.release(st_free)
    assert dev.is_assigned is False
    assert dev.is_available() is True
    assert dev.user is None
