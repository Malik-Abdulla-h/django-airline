from django.contrib import admin
from .models import Airport, Flight, Passenger 

class FlightAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'duration')

# Register your models here.
class Passengeradmin(admin.ModelAdmin):
    filter_horizontal = ('flights',)
 
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, Passengeradmin)  
# Assuming Passenger is also defined in models.py

