from datetime import date

device_name = "Ноутбук ASUS ROG OMAGAAD"
inventory_number = 10195
purchase_year = 2021
is_assigned = False  
last_maintenance_year = 2023
current_year = date.today().year


# Функция 1: Проверка доступности устройства к выдаче
def check_availability(is_assigned: bool) -> str:
    if not is_assigned:
        return "Устройство свободно"
    return "Устройство закреплено"


# Функция 2: Расчет возраста устройства
def calculate_age(purchase_year: int, current_year: int) -> int:
    return current_year - purchase_year


# Функция 3: Определение необходимости ТО
def check_maintenance(last_maintenance_year: int, current_year: int) -> str:
    years_since_service = current_year - last_maintenance_year
    if years_since_service >= 2:
        return "Требуется проведение технического обслуживания"
    return "Оборудование исправно, обслуживание не требуется"


# Вывод информации в консоль
print(f"Оборудование: {device_name} (Инв. № {inventory_number})")
print(f"Год закупки: {purchase_year}")
print(check_availability(is_assigned))
print(f"Срок эксплуатации: {calculate_age(purchase_year, current_year)} лет")
print(check_maintenance(last_maintenance_year, current_year))