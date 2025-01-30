import atexit
import time
import logging
from playwright.sync_api import sync_playwright

logger = logging.getLogger(__name__)


class BrowserManager:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None
        self.__init_playwright()

    def __init_playwright(self, headless=False):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.page = self.browser.new_page()

    def end_playwright(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

        # atexit.register(lambda: browser_playwright.end_playwright())

    def goto(self, url: str):
        if not self.browser:
            raise Exception("Browser not initialized.")

        self.page.goto(url)
        self.track_navigation()

    def track_navigation(self):
        if not self.page:
            return

        def log_event(frame):
            if frame.url:
                # from apps.base.models import NavigationLog

                url = frame.url
                logger.info(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Usuário navegou para: {url}")
                # NavigationLog.objects.create(url=url)

        # Captura eventos de navegação no Playwright
        self.page.on("framenavigated", log_event)


# Criar uma única instância global de Playwright
# browser_playwright = BrowserManager()
