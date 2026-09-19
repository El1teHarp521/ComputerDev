def add_device(
    devices: list[dict], name: str, inv_number: int, purchase_year: int
) -> dict:
    """Добавить новое устройство в список."""
    new_id = max([d["id"] for d in devices], default=0) + 1
    device = {
        "id": new_id,
        "name": name,
        "inventory_number": inv_number,
        "purchase_year": purchase_year,
        "last_maintenance_year": purchase_year,
    }
    devices.append(device)
    return device


def find_devices(devices: list[dict], query: str) -> list[dict]:
    """Поиск устройств по подстроке в названии."""
    q = query.lower()
    return [d for d in devices if q in d["name"].lower()]


def calculate_age(purchase_year: int, current_year: int) -> int:
    """Расчет срока эксплуатации устройства."""
    return current_year - purchase_year


def check_maintenance(last_maintenance_year: int, current_year: int) -> str:
    """Проверка необходимости ТО."""
    if (current_year - last_maintenance_year) >= 2:
        return "Требуется ТО"
    return "Исправно"


def sort_devices_by_year(devices: list[dict]) -> list[dict]:
    """Сортировка устройств по году закупки."""
    return sorted(devices, key=lambda d: d["purchase_year"])
