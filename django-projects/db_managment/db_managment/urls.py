"""db_managment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include

from django.contrib.auth.views import LoginView

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('unicorn-app/', include('unicornapp.urls', namespace='unicornapp')),
    
    # Players App 
    path('', include('players.urls', namespace='players')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    
    
    path('admin/', admin.site.urls),
    
    
    
    path('main/', include('main_app.urls', namespace='main_app')),
    
    
    path('posts/', include('articles.urls', namespace='articles')),
    path('__debug__/', include('debug_toolbar.urls')),
    
    # AJAX - reactive Unicorn app 
    path("unicorn/", include("django_unicorn.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,  document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)