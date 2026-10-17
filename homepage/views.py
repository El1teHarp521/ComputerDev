from django.http import HttpResponse


def page(title: str, content: str) -> str:
    """Генерация базового HTML-каркаса страницы с Bootstrap 5.3."""
    bootstrap = (
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3"
        "/dist/css/bootstrap.min.css"
    )
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="{bootstrap}">
</head>
<body class="bg-light">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">ComputerDev</a>
            <div class="navbar-nav">
                <a class="nav-link" href="/">Главная</a>
                <a class="nav-link" href="/devices/">Устройства</a>
                <a class="nav-link" href="/assignments/">Выдачи техники</a>
            </div>
        </div>
    </nav>
    <main class="container">{content}</main>
</body>
</html>"""


def index(request) -> HttpResponse:
    """Главная страница веб-приложения."""
    content = """
    <div class="p-5 mb-4 bg-white rounded-3 shadow-sm">
        <h1 class="display-5 fw-bold">Учет компьютерных устройств</h1>
        <p class="fs-4 text-muted">
            Веб-интерфейс для инвентаризации оборудования, контроля статусов
            и выдачи техники сотрудникам.
        </p>
        <div class="d-flex gap-2">
            <a href="/devices/" class="btn btn-primary btn-lg">Устройства</a>
            <a href="/assignments/" class="btn btn-secondary btn-lg">Выдачи</a>
        </div>
    </div>
    """
    return HttpResponse(page("Главная — Учет устройств", content))


def page_not_found(request, exception) -> HttpResponse:
    """Кастомная страница ошибки 404."""
    content = """
    <div class="text-center py-5">
        <h1 class="display-1 text-danger fw-bold">404</h1>
        <h2>Страница не найдена</h2>
        <p class="lead text-muted">
            Запрошенный ресурс не существует или был перемещен.
        </p>
        <a href="/" class="btn btn-primary">Вернуться на главную</a>
    </div>
    """
    return HttpResponse(
        page("404 — Страница не найдена", content), status=404
    )
