"""SDSDiamonds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from SDSDiamonds import settings
from django.conf.urls.static import static
from django.views.static import serve
from firstapp import views as dash_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstapp.urls')),
    path('tinymce/', include('tinymce.urls')),

    # User specific
    path('', include('user.urls.common_urls')),
    path('', include('user.urls.colorstone_urls')),
    path('', include('user.urls.diamond_urls')),
    path('', include('user.urls.jewellery_urls')),
    path('', include('user.urls.blog_urls')),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
