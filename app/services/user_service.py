from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise Exception('User not found')
        return user

    def create_user(self, data):
        username = data.get('username')
        email = data.get('email')
        if not username or not email:
            raise ValueError('Missing username or email')
        
        return self.user_repository.create_user(username, email)
