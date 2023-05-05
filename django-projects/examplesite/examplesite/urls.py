
from django.contrib import admin
from django.urls import path,include
from main.views import homePageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePageView, name='home'),
    path('accounts/', include('allauth.urls')),
]
