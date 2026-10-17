from django.http import HttpResponse
from homepage.views import page
from storage import load_all_data


def assignments_list(request) -> HttpResponse:
    """Список выданного сотрудникам оборудования."""
    _, _, _, devices = load_all_data()
    assigned = [d for d in devices if d.is_assigned]

    if not assigned:
        items = "<li class='list-group-item text-muted'>Нет активных выдач техники.</li>"
    else:
        items = ""
        for d in assigned:
            items += f"""
            <li class="list-group-item d-flex justify-content-between align-items-center">
                <div>
                    <a href="/assignments/{d.id}/" class="fw-bold text-decoration-none">
                        {d.name}
                    </a>
                    <span class="text-muted ms-2">→ {d.user.name}</span>
                </div>
                <span class="badge bg-primary">В эксплуатации</span>
            </li>
            """

    content = f"""
    <h1 class="mb-4">Выданное оборудование</h1>
    <ul class="list-group shadow-sm">{items}</ul>
    """
    return HttpResponse(page("Активные выдачи", content))


def assignment_detail(request, device_id: int) -> HttpResponse:
    """Детальная информация о выдаче оборудования."""
    _, _, _, devices = load_all_data()
    device = next((d for d in devices if d.id == device_id and d.is_assigned), None)

    if device is None:
        content = """
        <div class="alert alert-danger" role="alert">
            <h4 class="alert-heading">Выдача не найдена!</h4>
            <p>Устройство не выдано или отсутствует в базе данных.</p>
            <hr>
            <a href="/assignments/" class="btn btn-outline-danger">← Назад к списку</a>
        </div>
        """
        return HttpResponse(page("Выдача не найдена", content), status=404)

    content = f"""
    <div class="card shadow-sm border-info">
        <div class="card-header bg-info text-dark">
            <h4 class="mb-0">Запись о выдаче: {device.name}</h4>
        </div>
        <div class="card-body">
            <p class="card-text"><strong>Инвентарный номер:</strong> {device.inventory_number}</p>
            <p class="card-text"><strong>Категория:</strong> {device.category.name}</p>
            <p class="card-text"><strong>Ответственный сотрудник:</strong> {device.user.name}</p>
            <p class="card-text"><strong>Почта сотрудника:</strong> {device.user.email}</p>
            <a href="/assignments/" class="btn btn-outline-secondary mt-3">← Ко всем выдачам</a>
        </div>
    </div>
    """
    return HttpResponse(page(f"Выдача — {device.name}", content))
