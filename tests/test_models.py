from models import Category, State


def test_category_creation():
    cat = Category(1, "Ноутбуки")
    assert cat.id == 1
    assert str(cat) == "Ноутбуки"


def test_category_from_data():
    data = {"id": 2, "name": "Мониторы"}
    cat = Category.from_data(data)
    assert cat.id == 2
    assert cat.name == "Мониторы"


def test_state_creation():
    st = State(1, "Свободно к выдаче", True)
    assert st.id == 1
    assert st.is_available is True
    assert str(st) == "Свободно к выдаче"
