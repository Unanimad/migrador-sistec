from django.http import JsonResponse

from apps.base.domain import browser_playwright


def sistec_login(request):
    try:
        browser_playwright.goto("https://sistec.mec.gov.br/login")
        return JsonResponse({"status": "success", "message": "Navegação iniciada"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
