from abc import ABC, abstractmethod
from app.models.user import User

class AUserService(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def create_user(self, data: dict) -> User:
        pass
