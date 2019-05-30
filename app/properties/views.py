from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View, generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


from .models import Property, PropertyType
from .forms import SearchPropertyForm


import logging
logger = logging.getLogger(__name__)


def other_page(request):
    context = {
        'test': 'passing a value to the template'
    }
    return render(request, 'samples/other.html', context)


class PropertyCreateView(generic.CreateView):
    model = Property
    fields = ['name', 'description', 'type', 'street',
        'building', 'apartment', 'city']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(PropertyCreateView, self).form_valid(form)


class PropertyUpdateView(generic.UpdateView):
    model = Property
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('detail', args=[self.kwargs['pk']])


class PropertyListView(generic.ListView):
    model = Property
    form_class = SearchPropertyForm

    def get_queryset(self):
        queryset = super(PropertyListView, self).get_queryset()
        
        form = self.form_class(self.request.GET)
        if form.is_valid():
            data = form.cleaned_data
            logger.warn(data)
            return queryset.filter(
                city__icontains=data['city'],
                capacity__gte=data['people']
            )
        return queryset


class BookView(LoginRequiredMixin, generic.DetailView):
    model = Property


class PropertyDetailView(generic.DetailView):
    model = Property


class AboutView(generic.TemplateView):
    template_name = 'samples/about.html'

    def get_context_data(self):
        context = {'dynamic_val': 'this info changes'}
        return context
