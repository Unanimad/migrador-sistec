import os
import threading
from django.apps import AppConfig

from . import browser_playwright


class BaseConfig(AppConfig):
    name = 'apps.base'

    def ready(self):
        if os.environ.get('DJANGO_SETTINGS_MODULE') and not any(arg.startswith('createsuperuser') for arg in os.sys.argv):
            def start_playwright():
                browser_playwright.init_playwright()
                browser_playwright.page.goto("http://localhost:8000")

            threading.Thread(target=start_playwright, daemon=True).start()
