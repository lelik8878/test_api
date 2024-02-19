from django.urls import path

from .views import get_fetch_articles

urlpatterns = [
    path('', get_fetch_articles)

]