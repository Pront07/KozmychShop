from django.shortcuts import render, HttpResponse

from .mixins import DetailViewBreadcrumbMixin
from .models import Page
from .interfaces import NewsInfo
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def news(request):
    return render(request, 'main/news.html')

def about(request):
    return render(request, 'main/about.html')


class PageDetailView(DetailViewBreadcrumbMixin):
    model = Page
    template_name = 'main/page.html'
    context_object_name = 'page'
    
    
    def get_breradcrumb(self):
        return {self.object.get_absolute_url(): self.object.name}


def news(request):
    all_clothing_news = NewsInfo.get_clothing_brand_news()
    return render(request, 'main/news.html', {'all_clothing_news': all_clothing_news})
