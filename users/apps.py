from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    # import signals (to automatically create Profile for new saved User )
    def ready(self):
        import users.signals
