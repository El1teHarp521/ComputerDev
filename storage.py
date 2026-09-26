import json
import os
from typing import Optional
from models import Category, State, User, Device


def load_raw_json(filepath: str) -> list[dict]:
    """Чтение сырых данных из JSON с защитой от ошибок."""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_raw_json(filepath: str, data: list[dict]) -> None:
    """Запись данных в JSON."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_all_data():
    """Загрузка всех сущностей и построение объектных связей."""
    cats_data = load_raw_json("data/categories.json")
    states_data = load_raw_json("data/states.json")
    users_data = load_raw_json("data/users.json")
    devs_data = load_raw_json("data/devices.json")

    categories = [Category.from_data(c) for c in cats_data]
    states = [State.from_data(s) for s in states_data]
    users = [User.from_data(u) for u in users_data]

    cat_map = {c.id: c for c in categories}
    state_map = {s.id: s for s in states}
    user_map = {u.id: u for u in users}

    devices: list[Device] = []
    for d in devs_data:
        cat = cat_map.get(d["category_id"], Category(0, "Без категории"))
        st = state_map.get(d["state_id"], State(0, "Неизвестно", False))
        usr: Optional[User] = user_map.get(d.get("user_id"))
        devices.append(
            Device(
                device_id=d["id"],
                name=d["name"],
                inventory_number=d["inventory_number"],
                category=cat,
                state=st,
                user=usr,
            )
        )
    return categories, states, users, devices


def save_devices(devices: list[Device]) -> None:
    """Преобразование объектов Device в JSON с сохранением ID связей."""
    data = []
    for d in devices:
        data.append(
            {
                "id": d.id,
                "name": d.name,
                "inventory_number": d.inventory_number,
                "category_id": d.category.id,
                "state_id": d.state.id,
                "user_id": d.user.id if d.user else None,
            }
        )
    save_raw_json("data/devices.json", data)
