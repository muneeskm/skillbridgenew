from django.apps import AppConfig

class SkillBridgeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'skillBridgeApp'

    def ready(self):
        import skillBridgeApp.signals