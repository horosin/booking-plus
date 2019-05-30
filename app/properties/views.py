from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views import View, generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q


from .models import Property, PropertyType, Booking
from .forms import SearchPropertyForm


import logging
logger = logging.getLogger(__name__)


def get_bookings_for_property(prop, date_from, date_to):
    return prop.booking_set.filter(
        Q(
            date_from__gte=date_from,
            date_from__lte=date_to
        ) |
        Q(
            date_to__gte=date_from,
            date_to__lte=date_to
        ) |
        Q(
            date_from__lte=date_from,
            date_to__gte=date_to
        )
    )


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
        if not form.is_valid():
            return queryset

        data = form.cleaned_data

        queryset = queryset.filter(
            city__icontains=data['city'],
            capacity__gte=data['people']
        )

        # Filter booking for following conditions
        # booking starts anywhere between us
        # booking ends anywhere between us
        # booking starts before us and ends after us
        available_ids = []
        for prop in queryset:
            bookings_nb = get_bookings_for_property(
                prop, data['date_from'], data['date_to']).count()
            if bookings_nb == 0:
                available_ids.append(prop.id)

        return queryset.filter(id__in=available_ids)


class PropertyDetailView(generic.DetailView):
    model = Property


class AboutView(generic.TemplateView):
    template_name = 'properties/about.html'

    def get_context_data(self):
        context = {'dynamic_val': 'this info changes'}
        return context


class BookView(View):

    def get(self, request, *args, **kwargs):
        prop = get_object_or_404(Property, pk=self.kwargs['pk'])

        context = {
            'object': prop,
            'date_from': self.kwargs['date_from'],
            'date_to': self.kwargs['date_to']
        }

        if get_bookings_for_property(prop, context['date_from'], context['date_to']).count() != 0:
            raise Http404("Property is not available at this time!")
        
        if request.GET.get('confirm'):
            Booking.objects.create(
                property=prop,
                user=request.user,
                # datetime.datetime.strptime(self.kwargs['date_from'], '%Y-%m-%d)
                date_from=self.kwargs['date_from'],
                date_to=self.kwargs['date_to']
            )
            context['confirm'] = True

        return render(request, 'properties/book.html', context)
