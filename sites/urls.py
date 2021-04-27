from django.urls import path
from .views import add_view


urlpatterns = [
    path('add-view/', add_view)
]