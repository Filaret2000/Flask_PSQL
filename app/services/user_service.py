from repositories.abstract.user_repository_interface import UserRepositoryInterface
from services.abstract.user_service_interface import UserServiceInterface
from typing import Optional, List
from models.user import User

class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository
        
    def get_all_users(self) -> List[User]:
        return self.user_repository.get_all_users()

    def get_user(self, user_id) -> User:
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise Exception('User not found')
        return user

    def create_user(self, data) -> User:
        username = data.get('username')
        email = data.get('email')
        if not username or not email:
            raise ValueError('Missing username or email')
        
        return self.user_repository.create_user(username, email)
        
    def update_user(self, user_id: int, data: dict) -> User:
        username = data.get('username')
        email = data.get('email')
        
        if not username or not email:
            raise ValueError('Missing username or email')
            
        user = self.user_repository.update_user(user_id, username, email)
        if not user:
            raise Exception('User not found')
        return user
        
    def delete_user(self, user_id: int) -> bool:
        result = self.user_repository.delete_user(user_id)
        if not result:
            raise Exception('User not found')
        return result
