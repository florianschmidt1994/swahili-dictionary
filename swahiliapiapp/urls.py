from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('en-sw/<str:searchterm>', views.english_swahili, name='search'),
    path('sw-en/<str:searchterm>', views.swahili_english, name='search'),
]