from django.contrib import admin

# Register your models here.
from .models import Airport, Flight, Passenger  
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)  
# Assuming Passenger is also defined in models.py

