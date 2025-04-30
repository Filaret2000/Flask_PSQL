from abc import ABC, abstractmethod
from typing import Optional, List
from models.user import User

class UserRepositoryInterface(ABC):
    @abstractmethod
    def get_all_users(self) -> List[User]:
        """Get all users."""
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Get a user by their ID."""
        pass

    @abstractmethod
    def create_user(self, username: str, email: str) -> User:
        """Create a new user."""
        pass
        
    @abstractmethod
    def update_user(self, user_id: int, username: str, email: str) -> Optional[User]:
        """Update an existing user."""
        pass
        
    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        """Delete a user by their ID."""
        pass