class State:
    """Сущность состояния (статуса) устройства."""

    def __init__(
        self, state_id: int, name: str, is_available: bool = True
    ) -> None:
        self.id = state_id
        self.name = name
        self.is_available = is_available

    def __str__(self) -> str:
        return self.name

    @classmethod
    def from_data(cls, data: dict) -> "State":
        return cls(
            state_id=data["id"],
            name=data["name"],
            is_available=data.get("is_available", True),
        )
