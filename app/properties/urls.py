from django.urls import path

from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('create/', views.PropertyCreateView.as_view(), name='create'),
    path('book/<int:pk>/<date_from>/<date_to>/', views.BookView.as_view(), name='book'),
    path('', views.PropertyListView.as_view(), name='index'),
]
