class User:
    """Сущность пользователя/сотрудника."""

    def __init__(self, user_id: int, name: str, email: str) -> None:
        self.id = user_id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"

    @classmethod
    def from_data(cls, data: dict) -> "User":
        return cls(
            user_id=data["id"],
            name=data["name"],
            email=data["email"],
        )
