import atexit
import time
import logging
from concurrent.futures import ThreadPoolExecutor
from playwright.sync_api import sync_playwright

logger = logging.getLogger(__name__)

executor = ThreadPoolExecutor(max_workers=1)  # Garantir que Playwright roda na mesma thread


class BrowserManager:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None
        self.init_playwright()

    def init_playwright(self, headless=False):
        def _start_playwright():
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=headless)
            self.page = self.browser.new_page()

        executor.submit(_start_playwright).result()  # Executar na thread correta

    def end_playwright(self):
        def _close_browser():
            if self.browser:
                self.browser.close()
            if self.playwright:
                self.playwright.stop()

        executor.submit(_close_browser).result()

    def goto(self, url: str):
        if not self.browser:
            raise Exception("Browser not initialized.")

        def _navigate():
            self.page.goto(url)
            self.track_navigation()

        executor.submit(_navigate).result()  # Garante que execute na thread correta

    def track_navigation(self):
        if not self.page:
            return

        def log_event(frame):
            if frame.url:
                from apps.base.models import NavigationLog

                url = frame.url
                logger.info(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Usuário navegou para: {url}")
                NavigationLog.objects.create(url=url)

        # Captura eventos de navegação no Playwright
        self.page.on("framenavigated", log_event)

# Criar uma única instância global de Playwright
browser_playwright = BrowserManager()

# Fechar Playwright corretamente ao encerrar o Django
atexit.register(lambda: browser_playwright.end_playwright())
