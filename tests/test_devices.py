from devices import (
    add_device,
    find_devices,
    calculate_age,
    sort_devices_by_year,
)


def test_add_device():
    devices = []
    dev = add_device(devices, "Ноутбук Asus", 55501, 2023)
    assert len(devices) == 1
    assert dev["id"] == 1
    assert dev["name"] == "Ноутбук Asus"


def test_find_devices():
    devices = [
        {
            "id": 1,
            "name": "Монитор Dell",
            "inventory_number": 1,
            "purchase_year": 2022,
            "last_maintenance_year": 2022,
        },
        {
            "id": 2,
            "name": "ПК Lenovo",
            "inventory_number": 2,
            "purchase_year": 2023,
            "last_maintenance_year": 2023,
        },
    ]
    result = find_devices(devices, "dell")
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_calculate_age():
    assert calculate_age(2020, 2026) == 6


def test_sort_devices_by_year():
    devices = [
        {"id": 1, "name": "A", "purchase_year": 2024},
        {"id": 2, "name": "B", "purchase_year": 2021},
    ]
    sorted_res = sort_devices_by_year(devices)
    assert sorted_res[0]["purchase_year"] == 2021
