from datetime import date


def is_device_assigned(assignments: list[dict], device_id: int) -> bool:
    """Проверяет, закреплено ли устройство за сотрудником."""
    for item in assignments:
        if item["device_id"] == device_id:
            return True
    return False


def get_assignment_status(is_assigned: bool) -> str:
    """Текстовый статус доступности устройства."""
    if not is_assigned:
        return "Устройство свободно и готово к выдаче"
    return "Устройство уже закреплено за сотрудником"


def assign_device(
    assignments: list[dict], device_id: int, employee: str
) -> dict | None:
    """Закрепить устройство за сотрудником."""
    if is_device_assigned(assignments, device_id):
        return None
    new_id = max([a["id"] for a in assignments], default=0) + 1
    record = {
        "id": new_id,
        "device_id": device_id,
        "employee": employee,
        "date": str(date.today()),
    }
    assignments.append(record)
    return record


def return_device(assignments: list[dict], device_id: int) -> bool:
    """Оформить возврат устройства."""
    for index, item in enumerate(assignments):
        if item["device_id"] == device_id:
            assignments.pop(index)
            return True
    return False
