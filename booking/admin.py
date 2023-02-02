from django.contrib import admin
from .models import Customer, Guest, Reservation, Room, GuestDetail
# Register your models here.
admin.site.register(Customer)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(GuestDetail)

