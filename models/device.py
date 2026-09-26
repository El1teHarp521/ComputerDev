from typing import Optional
from .category import Category
from .state import State
from .user import User


class Device:
    """Сущность компьютерного устройства."""

    def __init__(
        self,
        device_id: int,
        name: str,
        inventory_number: int,
        category: Category,
        state: State,
        user: Optional[User] = None,
    ) -> None:
        self.id = device_id
        self.name = name
        self.inventory_number = inventory_number
        self.category = category
        self.state = state
        self.user = user

    @staticmethod
    def validate_inv_number(inv: int) -> bool:
        """Проверка корректности инвентарного номера."""
        return inv > 0

    @property
    def is_assigned(self) -> bool:
        """Свойство: закреплено ли устройство за кем-то."""
        return self.user is not None

    def is_available(self) -> bool:
        """Проверка доступности устройства к выдаче."""
        return not self.is_assigned and self.state.is_available

    def assign_to_user(self, user: User, busy_state: State) -> None:
        """Закрепить устройство за сотрудником и изменить состояние."""
        self.user = user
        self.state = busy_state

    def release(self, free_state: State) -> None:
        """Освободить устройство."""
        self.user = None
        self.state = free_state

    def set_maintenance(self, maint_state: State) -> None:
        """Перевести устройство в состояние техобслуживания."""
        self.user = None
        self.state = maint_state

    def __str__(self) -> str:
        holder = self.user.name if self.user else "Свободно"
        return (
            f"[{self.id}] {self.name} (Инв. {self.inventory_number}) | "
            f"Категория: {self.category} | Статус: {self.state} | "
            f"Закреплено: {holder}"
        )
