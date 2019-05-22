from django.urls import path

from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('other/', views.other_page, name='other'),
    path('<int:pk>/', views.HotelDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.HotelUpdateView.as_view(), name='update'),
    path('create/', views.HotelCreateView.as_view(), name='create'),
    path('about/', TemplateView.as_view(template_name="samples/about.html"), name='about'),
    path('about-class/', views.AboutView.as_view(), name='about_class'),
    path('', views.HotelListView.as_view(), name='index'),
]
