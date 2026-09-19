from datetime import date
from storage import load_data, save_data
from utils import input_int
from devices import (
    add_device,
    find_devices,
    calculate_age,
    check_maintenance,
    sort_devices_by_year,
)
from assignments import (
    is_device_assigned,
    get_assignment_status,
    assign_device,
    return_device,
)

DEVICES_FILE = "data/devices.json"
ASSIGNMENTS_FILE = "data/assignments.json"


def show_devices(devices: list[dict], assignments: list[dict]) -> None:
    """Вывести список всех устройств в виде таблицы."""
    if not devices:
        print("Список устройств пуст.")
        return
    current_year = date.today().year
    header = (
        f"\n{'ID':<3} | {'Название':<25} | {'Инв. №':<8} | "
        f"{'Возраст':<8} | {'ТО':<12} | {'Статус'}"
    )
    print(header)
    print("-" * 80)
    for d in devices:
        assigned = is_device_assigned(assignments, d["id"])
        status = "Выдано" if assigned else "Свободно"
        age = f"{calculate_age(d['purchase_year'], current_year)} лет"
        maint = check_maintenance(d["last_maintenance_year"], current_year)
        print(
            f"{d['id']:<3} | {d['name']:<25} | {d['inventory_number']:<8} | "
            f"{age:<8} | {maint:<12} | {status}"
        )


def show_assignments(assignments: list[dict], devices: list[dict]) -> None:
    """Вывести текущие выдачи оборудования."""
    if not assignments:
        print("\nНет активных выдач устройств.")
        return
    dev_names = {d["id"]: d["name"] for d in devices}
    header = (
        f"\n{'ID':<3} | {'Устройство':<25} | "
        f"{'Сотрудник':<18} | {'Дата выдачи'}"
    )
    print(header)
    print("-" * 65)
    for a in assignments:
        name = dev_names.get(a["device_id"], "Неизвестное устройство")
        print(f"{a['id']:<3} | {name:<25} | {a['employee']:<18} | {a['date']}")


def main() -> None:
    devices = load_data(DEVICES_FILE)
    assignments = load_data(ASSIGNMENTS_FILE)

    while True:
        print("\n=== СИСТЕМА УЧЕТА КОМПЬЮТЕРНЫХ УСТРОЙСТВ ===")
        print("1. Показать список всех устройств")
        print("2. Найти устройство по названию")
        print("3. Добавить новое устройство")
        print("4. Проверить статус устройства (ПР1 сценарий)")
        print("5. Выдать устройство сотруднику")
        print("6. Оформить возврат устройства")
        print("7. Показать активные выдачи")
        print("8. Показать устройства, отсортированные по году")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_devices(devices, assignments)

        elif choice == "2":
            q = input("Введите название или часть названия: ").strip()
            found = find_devices(devices, q)
            show_devices(found, assignments)

        elif choice == "3":
            name = input("Введите наименование: ").strip()
            inv = input_int("Введите инвентарный номер: ")
            year = input_int("Введите год закупки: ")
            add_device(devices, name, inv, year)
            save_data(DEVICES_FILE, devices)
            print("Устройство успешно сохранено!")

        elif choice == "4":
            dev_id = input_int("Введите ID устройства: ")
            assigned = is_device_assigned(assignments, dev_id)
            print(f"Статус: {get_assignment_status(assigned)}")

        elif choice == "5":
            dev_id = input_int("Введите ID устройства для выдачи: ")
            emp = input("ФИО сотрудника: ").strip()
            res = assign_device(assignments, dev_id, emp)
            if res:
                save_data(ASSIGNMENTS_FILE, assignments)
                print("Устройство успешно выдано!")
            else:
                print("Ошибка: устройство уже выдано кому-то другому!")

        elif choice == "6":
            dev_id = input_int("Введите ID устройства для возврата: ")
            if return_device(assignments, dev_id):
                save_data(ASSIGNMENTS_FILE, assignments)
                print("Возврат зафиксирован, устройство снова свободно!")
            else:
                print("Ошибка: устройство не числится в выданных.")

        elif choice == "7":
            show_assignments(assignments, devices)

        elif choice == "8":
            sorted_devs = sort_devices_by_year(devices)
            show_devices(sorted_devs, assignments)

        elif choice == "0":
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Повторите ввод.")


if __name__ == "__main__":
    main()
