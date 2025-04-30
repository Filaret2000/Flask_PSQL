from repositories.abstract.user_repository_interface import UserRepositoryInterface
from services.abstract.user_service_interface import UserServiceInterface
from typing import Optional, List
from models.user import User
from models.DTOs import UserDTO

class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository
        
    def get_all_users(self) -> List[UserDTO]:
        users = self.user_repository.get_all_users()
        return [UserDTO.from_entity(user) for user in users]

    def get_user(self, user_id) -> UserDTO:
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise Exception('User not found')
        return UserDTO.from_entity(user)

    def create_user(self, data) -> UserDTO:
        username = data.get('username')
        email = data.get('email')
        if not username or not email:
            raise ValueError('Missing username or email')
        
        # Create a DTO from request data
        create_dto = User(username=username, email=email)
        
        # Pass data to repository
        user = self.user_repository.create_user(create_dto)
        
        # Return DTO
        return UserDTO.from_entity(user)
        
    def update_user(self, user_id: int, data: dict) -> UserDTO:
        username = data.get('username')
        email = data.get('email')
        
        if not username or not email:
            raise ValueError('Missing username or email')
            
        # Create a DTO from request data
        update_dto = User(username=username, email=email)
        
        # Pass data to repository
        user = self.user_repository.update_user(user_id, update_dto)
        if not user:
            raise Exception('User not found')
            
        # Return DTO
        return UserDTO.from_entity(user)
        
    def delete_user(self, user_id: int) -> bool:
        result = self.user_repository.delete_user(user_id)
        if not result:
            raise Exception('User not found')
        return result
