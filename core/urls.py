"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers


from apps.api.views import ProfileViewSet
from apps.api.blog.views import PostViewSet
from apps.api.catalog.views import ProductViewSet

routers = routers.DefaultRouter()
routers.register(r'profiles', ProfileViewSet)
routers.register(r'posts', PostViewSet)
routers.register(r'products', ProductViewSet)


urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('captcha/', include('captcha.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/', include(routers.urls)),
    path('api/v2/', include('apps.api.urls')),

    path('admin/', admin.site.urls),
    path('members/', include('apps.members.urls')),
    path('reviews/', include('apps.blog.urls')),
    path('catalog/', include('apps.catalog.urls')),
    path('order/', include('apps.order.urls')),
    path('', include('apps.main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
