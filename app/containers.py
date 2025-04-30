from dependency_injector import containers, providers
from repositories.user_repository import UserRepository
from services.user_service import UserService

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["controllers"]
    )

    user_repository = providers.Singleton(UserRepository)
    user_service = providers.Factory(UserService, user_repository=user_repository)
