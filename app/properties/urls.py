from django.urls import path

from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('<int:pk>/', views.PropertyDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.PropertyUpdateView.as_view(), name='update'),
    path('create/', views.PropertyCreateView.as_view(), name='create'),
    path('about/', TemplateView.as_view(template_name="samples/about.html"), name='about'),
    path('about-class/', views.AboutView.as_view(), name='about_class'),
    path('book/<int:pk>/<date_from>/<date_to>/', views.BookView.as_view(), name='book'),
    path('', views.PropertyListView.as_view(), name='index'),
]
