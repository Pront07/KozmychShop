from django.views import generic
from django.db import models


class MetaTagMixin(models.Model):
    name = None
    meta_title = models.CharField(verbose_name="Мета заголовок", max_length=255, blank=True, null=True)
    meta_description = models.TextField(verbose_name="Мета опис", blank=True, null=True)
    meta_keywords = models.TextField(verbose_name="Ключові слова", blank=True, null=True)
    
    def get_meta_title(self):
        return self.meta_title or self.name # Якщо meta_title не вказано, то повертаємо name
    
    class Meta:
        abstract = True

class ListViewBreadcrumbMixin(generic.ListView):
    breadcrumbs = {}
    
    def get_breradcrumb(self):
        return self.breadcrumb
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breradcrumb()
        return context
    
class DetailViewBreadcrumbMixin(generic.DetailView):
    breadcrumbs = {}
    
    def get_breradcrumb(self):
        return self.breadcrumbs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breradcrumb()
        return context
    
    
