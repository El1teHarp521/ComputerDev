from django.http import HttpResponse
from homepage.views import page
from storage import load_all_data


def devices_list(request) -> HttpResponse:
    """Список всех компьютерных устройств."""
    _, _, _, devices = load_all_data()

    items = ""
    for dev in devices:
        badge = "bg-success" if dev.is_available() else "bg-secondary"
        items += f"""
        <li class="list-group-item d-flex justify-content-between align-items-center">
            <div>
                <a href="/devices/{dev.id}/" class="fw-bold text-decoration-none">
                    {dev.name}
                </a>
                <span class="text-muted ms-2">Инв. №{dev.inventory_number}</span>
                <span class="badge bg-info text-dark ms-2">{dev.category.name}</span>
            </div>
            <span class="badge {badge}">{dev.state.name}</span>
        </li>
        """

    content = f"""
    <h1 class="mb-4">Список оборудования</h1>
    <ul class="list-group shadow-sm">{items}</ul>
    """
    return HttpResponse(page("Список устройств", content))


def device_detail(request, device_id: int) -> HttpResponse:
    """Страница отдельного устройства по ID."""
    _, _, _, devices = load_all_data()
    device = next((d for d in devices if d.id == device_id), None)

    if device is None:
        content = """
        <div class="alert alert-danger" role="alert">
            <h4 class="alert-heading">Устройство не найдено!</h4>
            <p>Оборудование с указанным идентификатором отсутствует в базе данных.</p>
            <hr>
            <a href="/devices/" class="btn btn-outline-danger">← Назад к списку</a>
        </div>
        """
        return HttpResponse(page("Устройство не найдено", content), status=404)

    holder = (
        f"{device.user.name} ({device.user.email})"
        if device.user else "Оборудование свободно"
    )
    badge = "bg-success" if device.is_available() else "bg-warning text-dark"

    content = f"""
    <div class="card shadow-sm">
        <div class="card-header bg-primary text-white">
            <h4 class="mb-0">{device.name}</h4>
        </div>
        <div class="card-body">
            <p class="card-text"><strong>ID устройства:</strong> {device.id}</p>
            <p class="card-text"><strong>Инвентарный номер:</strong> {device.inventory_number}</p>
            <p class="card-text"><strong>Категория:</strong> {device.category.name}</p>
            <p class="card-text"><strong>Текущее состояние:</strong>
                <span class="badge {badge}">{device.state.name}</span>
            </p>
            <p class="card-text"><strong>Закреплено за:</strong> {holder}</p>
            <a href="/devices/" class="btn btn-outline-primary mt-3">← Ко всем устройствам</a>
        </div>
    </div>
    """
    return HttpResponse(page(f"{device.name} — Детали", content))
