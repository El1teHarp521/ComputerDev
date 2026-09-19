import json
import os


def load_data(filepath: str) -> list[dict]:
    """Загрузить список словарей из JSON-файла."""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_data(filepath: str, data: list[dict]) -> None:
    """Сохранить данные в JSON-файл."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
