from django.contrib import admin

from .models import Catalog, Product, Image
from django import forms


class ProductCategoryInline(admin.TabularInline):
    model = Product.category.through
    extra = 1


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('product', 'image_tag_thumbnail', 'image', 'is_main')
    readonly_fields = ('image_tag_thumbnail',)
    extra = 1


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_tag_thumbnail', 'is_main')
    readonly_fields = ('image_tag',)


# Register your models here.
@admin.register(Catalog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag_thumbnail')
    prepopulated_fields = {'slug': ('name',)}  # це поле автоматично заповнюється на основі іншого поля
    readonly_fields = ('image_tag_thumbnail',)  # це поле тільки для читання


class ProductAdminForm(forms.ModelForm):
    AVAILABLE_SIZES_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]

    available_sizes = forms.MultipleChoiceField(
        choices=AVAILABLE_SIZES_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Доступні розміри'
    )

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_display', 'created_at', 'updated_at', 'image_tag')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductCategoryInline, ImageInline]
    form = ProductAdminForm

