from abc import ABC, abstractmethod
from typing import Optional, List
from models.DTOs import UserDTO

class UserServiceInterface(ABC):
    @abstractmethod
    def get_all_users(self) -> List[UserDTO]:
        pass
        
    @abstractmethod
    def get_user(self, user_id: int) -> UserDTO:
        pass

    @abstractmethod
    def create_user(self, data: dict) -> UserDTO:
        pass
        
    @abstractmethod
    def update_user(self, user_id: int, data: dict) -> UserDTO:
        pass
        
    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass
