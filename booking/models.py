from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField
import random

# Create your models here.
class Room(models.Model):
    id = models.PositiveIntegerField(
        primary_key=True,
        blank=False,
        null=False,
        unique=True,
        default=0
    )
    room_number = models.IntegerField(blank=True, null=False, unique=True)
    room_name = models.CharField(max_length=255, blank=True, null=True)
    # Defining Room Type:
    default_answer = 0
    single = "SINGLE"
    double = "DOUBLE"
    family = "FAMILY"
    room_types = (
        (default_answer, "Default"),
        (single, "Single"),
        (double, "Double"),
        (family, "Family")
    )
    
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    
    room_type = models.CharField(max_length=10, choices=room_types, default=default_answer)
    
    #Room Availability
    yes = "YES"
    no = "NO"
    pending = "PENDING"
    is_available = (
        (yes, "YES"),
        (no, "NO"),
        (pending, "PENDING")
    )
    
    available = models.CharField(max_length=10, default=pending, blank=False, null=True, choices=is_available)
    
    def save(self, *args, **kwargs):
        self.room_name = self.room_type
        self.room_number = self.id
        
        if self.room_type == "SINGLE":
            self.price = 2000
        elif self.room_type == "DOUBLE":
            self.price = 5000
        elif self.room_type == "FAMILY":
            self.price = 7000
            
        super(Room, self).save(*args, **kwargs)
    
    def __str__(self):
        return "Room: {}| Number: {}| available: {}".format(self.room_name, self.room_number, self.available)

class Reservation(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=40,
        blank=False,
        null=False,
        unique=True,
        default=uuid.uuid4
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=False)
    number_of_people = models.IntegerField(blank=False, null=True)
    number_of_night = models.IntegerField(blank=False, null=True)
    details = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.room)

class Service(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    mini_bar = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    room_service = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return "{}".format(self.name)


class Customer(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(blank=True, null=False)
    phone_number = PhoneNumberField(null=False, blank=True, unique=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, blank=False, null=True)
    def __str__(self):
        return "{}".format(self.name)
    
class Guest(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(blank=True, null=False)
    phone_number = PhoneNumberField(null=False, blank=True, unique=True) 
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return "{}".format(self.name)

class Invoice(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=40,  
        blank=False,
        null=False,
        unique=True,
        default=uuid.uuid1
    )
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(blank=False, null=True)
    # Return name of Client
    name = models.CharField(max_length=255, blank=True, null=True)
    
    mini_bar = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    room_service = models.CharField(max_length=255, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=False)
    services = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=False)
    
    def save(self, *args, **kwargs):
        self.mini_bar = self.services.mini_bar
        self.room_service = self.services.room_service
        
        if self.customer:
            self.name = self.customer.name
        elif self.guest:
            self.name = self.guest.name
            
        super(Invoice, self).save(*args, **kwargs)
    
    
    def __str__(self):
        return "invoice: {}  ||  {}".format(self.id, self.date)
