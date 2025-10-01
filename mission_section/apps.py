from django.apps import AppConfig


class MissionSectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mission_section'
    
    def ready(self):
        # Импортируем модуль translation для регистрации моделей
        import mission_section.translation
