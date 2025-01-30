import threading

from apps.base.domain import BrowserManager
from apps.sistec.domain import SISTEC


# pytest apps/sistec/tests.py -v


def test_sistec_login():
    def run_playwright():
        browser_playwright = BrowserManager()
        sistec = SISTEC()
        result = sistec.login(browser_playwright)
        assert result["status"] == "success", "Login failed"
        browser_playwright.end_playwright()

    # Rodar a função de teste em uma thread separada
    thread = threading.Thread(target=run_playwright)
    thread.start()
    thread.join()
