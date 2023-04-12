from django.urls import path

from user_juridico.views import index


urlpatterns = [
    path('', index)
]