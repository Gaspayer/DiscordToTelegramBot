from django.apps import AppConfig
import threading
from .forwarder import start_discord_bot

class ForwarderAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forwarder_app'

    def ready(self):
        thread = threading.Thread(target=start_discord_bot, daemon=True)
        thread.start()
