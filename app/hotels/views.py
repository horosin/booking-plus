from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View, generic
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from .models import Hotel, HotelType


def other_page(request):
    context = {
        'test': 'passing a value to the template'
    }
    return render(request, 'samples/other.html', context)


class HotelCreateView(generic.CreateView):
    model = Hotel
    fields = '__all__'
    success_url = reverse_lazy('index')


class HotelUpdateView(generic.UpdateView):
    model = Hotel
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('detail', args=[self.kwargs['pk']])


class HotelListView(generic.ListView):
    model = Hotel


class HotelDetailView(generic.DetailView):
    model = Hotel


class AboutView(generic.TemplateView):
    template_name = 'samples/about.html'

    def get_context_data(self):
        context = {'dynamic_val': 'this info changes'}
        return context
