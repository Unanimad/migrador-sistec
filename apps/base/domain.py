import time
import logging

from playwright.sync_api import sync_playwright

logger = logging.getLogger(__name__)


class BrowserPlaywright:
    def __init__(self):
        self._playwright = None
        self.browser = None
        self.page = None

    def init_playwright(self, *args, **kwargs):
        headless = kwargs.get("headless", False)
        playwright = kwargs.get("playwright", None)
        if not playwright:
            self._playwright = sync_playwright().start()
        self.browser = self._playwright.chromium.launch(headless=headless)
        self.page = self.browser.new_page()
        if not headless:
            screen_width, screen_height = 1920, 1080
            self.page.set_viewport_size(
                {"width": screen_width, "height": screen_height}
            )

    def end_playwright(self):
        self.browser.close()
        self._playwright.stop()

    def goto(self, url: str):
        if not self.browser.page:
            self.browser.init_playwright()

        self.page.goto(url)
        self.track_navigation()

    def track_navigation(self):
        """Monitora a navegação do usuário dentro do SISTEC."""
        if not self.page:
            return

        def log_event(frame):
            """Função chamada quando o usuário navega para uma nova URL."""
            if frame.url:
                from apps.base.models import NavigationLog
                url = frame.url
                logger.info(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Usuário navegou para: {url}")
                NavigationLog.objects.create(url=url)

        # Captura eventos de navegação no Playwright
        self.page.on("framenavigated", log_event)
