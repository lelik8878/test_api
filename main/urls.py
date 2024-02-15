from django.urls import path

from .views import get_articles_list

urlpatterns = [
    path('get_articles_list/', get_articles_list)

]