from django.contrib import admin

from .models import PropertyType, Property


admin.site.site_header = 'Booking+ admin'

admin.site.register(Property)
admin.site.register(PropertyType)
