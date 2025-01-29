from apps.base.domain import BrowserManager


class SISTEC:
    url_login = "https://sistec.mec.gov.br/login/login"

    def login(self, browser: BrowserManager):
        try:
            browser.page.goto(self.url_login)
            browser.page.click("a[href*='sso.acesso.gov']")
            browser.page.wait_for_selector("input#accountId")
            browser.page.fill("input#accountId", "02777520518")
            browser.page.click("button:has-text('Continuar')")
            browser.page.wait_for_selector("iframe[title='Conteúdo principal do desafio hCaptcha']", state='detached')
            browser.page.fill("input#password", "296800@Ce")
            browser.page.click("button:has-text('Entrar')")
            browser.page.wait_for_load_state("load")

            # Verifica se a URL após login é a esperada
            if browser.page.url == "https://sistec.mec.gov.br/index/selecionarinstituicao/":
                return {"status": "success", "message": "Login successful."}
            else:
                return {"status": "error", "message": "Login failed. Unexpected URL."}
        except Exception as e:
            return {"status": "error", "message": str(e)}


sistec = SISTEC()
