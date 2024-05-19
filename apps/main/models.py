from django.db import models
from django.urls import reverse

from .mixins import MetaTagMixin

from ckeditor.fields import RichTextField


class Page(MetaTagMixin):
    name = models.CharField(verbose_name="Назва", max_length=255)
    slug = models.SlugField(verbose_name="URL", max_length=255, unique=True)
    content = RichTextField(verbose_name="Контент", blank=True, null=True)
    is_active = models.BooleanField(verbose_name="Активна", default=True)
    index = models.IntegerField(verbose_name="Індекс", default=-1, help_text="Вкажіть порядковий номер для сортування", blank=True)

    # Для дропдаун меню
    # parent = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name="Батьківська сторінка", null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Сторінка"
        verbose_name_plural = "Сторінки"
        ordering = ['index']
        
    def get_absolute_url(self):
        return reverse('main:page', kwargs={'slug': self.slug})