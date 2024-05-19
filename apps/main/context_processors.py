from .models import Page


def pages_navigation(request):
    pages = Page.objects.filter(is_active=True)
    return {'pages': pages}