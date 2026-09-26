class Category:
    """Сущность категории компьютерного оборудования."""

    def __init__(self, category_id: int, name: str) -> None:
        self.id = category_id
        self.name = name

    def __str__(self) -> str:
        return self.name

    @classmethod
    def from_data(cls, data: dict) -> "Category":
        return cls(category_id=data["id"], name=data["name"])
