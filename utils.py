def input_int(prompt: str) -> int:
    """Запросить у пользователя целое число."""
    while True:
        raw_val = input(prompt).strip()
        try:
            return int(raw_val)
        except ValueError:
            print("Ошибка: введите корректное целое число.")
