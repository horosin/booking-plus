from django.contrib import admin

from .models import HotelType, Hotel


admin.site.site_header = 'Lab admin'

admin.site.register(Hotel)
admin.site.register(HotelType)
