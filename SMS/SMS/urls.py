"""SMS URL Configuration

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
from django.conf import settings
from django.conf.urls.static  import static
from .views import home_view, register, logout_request, login_request, singleSlug, landing
from main.models import Difficulty, Puzzle
from main.views import DiffViewSet, PuzzViewSet
from profiles.models import Profile
from profiles.views import ProfileViewSet
from rest_framework import routers, serializers, viewsets

from rest_framework.authtoken.views import ObtainAuthToken
from django.views.decorators.csrf import csrf_exempt




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'category', DiffViewSet)
router.register(r'puzzles', PuzzViewSet)
router.register(r'users/(?P<username>[-\w]+)', ProfileViewSet, basename='Profile')



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.



app_name = "app"
urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', csrf_exempt(ObtainAuthToken.as_view())), #path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('app/', home_view, name="Home-View"),
    path('', landing, name="landing"),
    path('app/<single_slug>', singleSlug, name="single_slug"),
    path('', include('profiles.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('register', register, name="register"),
    path('logout/', logout_request, name="logout"),
    path('login/', login_request, name="login"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
