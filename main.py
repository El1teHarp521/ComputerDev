from models import Device
from storage import load_all_data, save_devices
from utils import input_int


def show_devices(devices: list[Device]) -> None:
    """Отображение всех устройств через метод __str__."""
    if not devices:
        print("Список устройств пуст.")
        return
    print("\n--- СПИСОК ОБОРУДОВАНИЯ ---")
    for d in devices:
        print(d)


def add_new_device(categories, states, devices: list[Device]) -> None:
    """Сценарий создания нового объекта Device."""
    print("\n--- Добавление устройства ---")
    name = input("Введите наименование: ").strip()
    inv = input_int("Введите инвентарный номер: ")
    if not Device.validate_inv_number(inv):
        print("Ошибка: инвентарный номер должен быть больше 0.")
        return

    print("\nВыберите категорию:")
    for c in categories:
        print(f"{c.id}. {c.name}")
    c_id = input_int("Номер категории: ")
    cat = next((c for c in categories if c.id == c_id), None)
    if not cat:
        print("Ошибка: категория не найдена.")
        return

    free_state = next(
        (s for s in states if s.name == "Свободно к выдаче"), states[0]
    )
    new_id = max([d.id for d in devices], default=0) + 1
    new_dev = Device(new_id, name, inv, cat, free_state)
    devices.append(new_dev)
    save_devices(devices)
    print(f"Устройство '{name}' успешно добавлено в базу!")


def assign_device_scenario(users, states, devices: list[Device]) -> None:
    """Сценарий закрепления устройства за сотрудником."""
    dev_id = input_int("Введите ID устройства для выдачи: ")
    device = next((d for d in devices if d.id == dev_id), None)
    if not device:
        print("Устройство не найдено.")
        return
    if not device.is_available():
        print(f"Ошибка: {device.name} недоступно (Статус: {device.state})")
        return

    print("\nВыберите сотрудника:")
    for u in users:
        print(f"{u.id}. {u}")
    u_id = input_int("ID сотрудника: ")
    user = next((u for u in users if u.id == u_id), None)
    if not user:
        print("Сотрудник не найден.")
        return

    busy_state = next(
        (s for s in states if s.name == "В эксплуатации"), states[1]
    )
    device.assign_to_user(user, busy_state)
    save_devices(devices)
    print(f"Устройство успешно выдано сотруднику {user.name}!")


def release_device_scenario(states, devices: list[Device]) -> None:
    """Сценарий возврата устройства на склад."""
    dev_id = input_int("Введите ID устройства для возврата: ")
    device = next((d for d in devices if d.id == dev_id), None)
    if not device:
        print("Устройство не найдено.")
        return
    if not device.is_assigned:
        print("Устройство и так не числится выданным.")
        return

    free_state = next(
        (s for s in states if s.name == "Свободно к выдаче"), states[0]
    )
    device.release(free_state)
    save_devices(devices)
    print("Устройство возвращено на склад и снова доступно к выдаче!")


def main() -> None:
    categories, states, users, devices = load_all_data()

    while True:
        print("\n=== УЧЕТ КОМПЬЮТЕРНЫХ УСТРОЙСТВ (ООП) ===")
        print("1. Показать список устройств")
        print("2. Добавить новое устройство")
        print("3. Выдать устройство сотруднику")
        print("4. Принять возврат устройства")
        print("5. Показать список пользователей")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_devices(devices)
        elif choice == "2":
            add_new_device(categories, states, devices)
        elif choice == "3":
            assign_device_scenario(users, states, devices)
        elif choice == "4":
            release_device_scenario(states, devices)
        elif choice == "5":
            print("\n--- СПИСОК ПОЛЬЗОВАТЕЛЕЙ ---")
            for u in users:
                print(u)
        elif choice == "0":
            print("Работа завершена.")
            break
        else:
            print("Некорректный выбор.")


if __name__ == "__main__":
    main()
