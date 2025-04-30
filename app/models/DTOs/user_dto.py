from dataclasses import dataclass
from typing import Optional


@dataclass
class UserDTO:
    """Data Transfer Object for User entity"""
    id: Optional[int] = None
    username: str = ""
    email: str = ""

    @classmethod
    def from_entity(cls, user):
        """Convert a User entity to UserDTO"""
        if not user:
            return None
        return cls(
            id=user.id,
            username=user.username,
            email=user.email
        )

    @classmethod
    def to_dict(cls, user_dto):
        """Convert UserDTO to dictionary"""
        if not user_dto:
            return None
        return {
            'id': user_dto.id,
            'username': user_dto.username,
            'email': user_dto.email
        }


@dataclass
class UpdateUserDTO:
    """DTO for updating an existing user"""
    username: str
    email: str
