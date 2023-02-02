from django.contrib import admin
from .models import Customer, Guest, Reservation, Room, Invoice, Service
# Register your models here.
admin.site.register(Customer)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(Invoice)
admin.site.register(Service)
