from assignments import is_device_assigned, assign_device, return_device


def test_assignment_cycle():
    assignments = []
    # 1. Сначала устройство свободно
    assert not is_device_assigned(assignments, device_id=1)

    # 2. Выдаем сотруднику
    assign_device(assignments, device_id=1, employee="Сидоров А.А.")
    assert is_device_assigned(assignments, device_id=1)

    # 3. Повторная выдача запрещена
    duplicate = assign_device(assignments, device_id=1, employee="Петров П.П.")
    assert duplicate is None

    # 4. Возврат устройства
    assert return_device(assignments, device_id=1)
    assert not is_device_assigned(assignments, device_id=1)
