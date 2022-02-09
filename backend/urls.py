"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import index_view, appjs_view, MessageViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [

    # http://localhost:8000/
    # These paths are for the Vue app - remove if you are not using the vue frontend, and create your custom views.
    path('', index_view, name='index'),
    path('app.js', appjs_view, name='appjs'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin123/', admin.site.urls),
]

# Matches everything else, probably a Vue route?
# urlpatterns += [
#     re_path(r'(?P<url>)$', index_view, name='index-for-SPA'),
# ]