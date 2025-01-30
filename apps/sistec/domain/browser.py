from apps.base.domain import BrowserManager


class SISTEC:
    url_base = "https://sistec.mec.gov.br/"

    def login(self, browser: BrowserManager):
        browser.page.goto(self.url_base + "login/login")
        browser.page.click("a[href*='sso.acesso.gov']")
        browser.page.wait_for_load_state("load")
        browser.page.wait_for_selector("input#accountId")
        browser.page.fill("input#accountId", "027.775.205-18")
        browser.page.click("button:has-text('Continuar')")
        browser.page.wait_for_selector("iframe[title='Conteúdo principal do desafio hCaptcha']", state='detached')
        browser.page.fill("input#password", "296800@Ce")
        browser.page.click("button:has-text('Entrar')")
        browser.page.wait_for_load_state("load")

        if browser.page.url == "https://sistec.mec.gov.br/index/selecionarinstituicao/":
            return {"status": "success", "message": "Login successful."}
        else:
            return {"status": "error", "message": "Login failed. Unexpected URL."}


sistec = SISTEC()
