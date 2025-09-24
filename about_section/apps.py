from django.apps import AppConfig


class AboutSectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about_section'
    verbose_name = 'Секция "О нас" и Партнеры'
    
    def ready(self):
        """Called when the app is ready"""
        # Import signals if needed
        # import about_section.signals
        pass
