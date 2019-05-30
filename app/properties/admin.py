from django.contrib import admin

from .models import PropertyType, Property, Booking


admin.site.site_header = 'Booking+ admin'

admin.site.register(Property)
admin.site.register(PropertyType)
admin.site.register(Booking)
