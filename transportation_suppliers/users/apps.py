from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "transportation_suppliers.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import transportation_suppliers.users.signals  # noqa F401
        except ImportError:
            pass
