from models.user import User
from config.db import db
from repositories.abstract.user_repository_interface import UserRepositoryInterface
from typing import Optional, List

class UserRepository(UserRepositoryInterface):
    def get_all_users(self) -> List[User]:
        return User.query.all()
        
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return User.query.get(user_id)

    def create_user(self, username: str, email: str) -> User:
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user
        
    def update_user(self, user_id: int, username: str, email: str) -> Optional[User]:
        user = self.get_user_by_id(user_id)
        if not user:
            return None
            
        user.username = username
        user.email = email
        db.session.commit()
        return user
        
    def delete_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)
        if not user:
            return False
            
        db.session.delete(user)
        db.session.commit()
        return True
