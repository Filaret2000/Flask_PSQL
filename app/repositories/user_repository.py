from models.user import User
from config.db import db
from repositories.abstract.user_repository_interface import UserRepositoryInterface
from typing import Optional, List

class UserRepository(UserRepositoryInterface):
    def get_all_users(self) -> List[User]:
        return User.query.all()
        
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return User.query.get(user_id)

    def create_user(self, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user
        
    def update_user(self, user_id: int, user: User) -> Optional[User]:
        old_user = self.get_user_by_id(user_id)
        if not old_user:
            return None
            
        old_user.username = user.username
        old_user.email = user.email
        db.session.commit()
        return old_user
        
    def delete_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)
        if not user:
            return False
            
        db.session.delete(user)
        db.session.commit()
        return True
