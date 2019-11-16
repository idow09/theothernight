from dependency_injector import providers, containers
from ui import ConsoleUI


class Interfaces(containers.DeclarativeContainer):
    console_ui = providers.Singleton(ConsoleUI)
