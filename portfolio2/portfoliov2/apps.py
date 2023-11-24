from django.apps import AppConfig


class Portfoliov2Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "portfoliov2"

    
    def ready(self):
        import portfoliov2.signals  
