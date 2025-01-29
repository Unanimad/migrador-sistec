from django.http import JsonResponse

from apps.base.domain import browser_playwright
from apps.sistec.domain import sistec


def sistec_login(request):
    try:
        # Inicializa o Playwright (se ainda não estiver inicializado)
        if not browser_playwright.playwright or not browser_playwright.browser or not browser_playwright.page:
            browser_playwright.init_playwright(headless=False)

        # Executa o login no SISTEC
        response = sistec.login(browser_playwright)

        # Retorna a resposta como JSON
        return JsonResponse(response)
    except Exception as e:
        # Em caso de erro, retorna uma mensagem de erro
        return JsonResponse({"status": "error", "message": str(e)})
