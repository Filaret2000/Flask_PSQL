from abc import ABC, abstractmethod
from typing import Optional, List
from models.user import User

class UserServiceInterface(ABC):
    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass
        
    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def create_user(self, data: dict) -> User:
        pass
        
    @abstractmethod
    def update_user(self, user_id: int, data: dict) -> User:
        pass
        
    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass
