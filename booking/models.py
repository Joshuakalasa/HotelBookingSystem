from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Room(models.Model):
    
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
    
    room_type = models.CharField(max_length=10, choices=room_types, default=default_answer)
    room_number = models.IntegerField(blank=False, null=False, unique=True)
    
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
        return "{} {}".format(self.room, self.details)

class GuestDetail(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=False)

class Customer(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(blank=True, null=False)
    phone_number = PhoneNumberField(null=False, blank=True, unique=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, blank=False, null=True)
    def __str__(self):
        return "{} {}".format(self.name, self.reservation)
    
class Guest(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(blank=True, null=False)
    phone_number = PhoneNumberField(null=False, blank=True, unique=True) 
    guest_details = models.ForeignKey(GuestDetail, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return "{}{}".format(self.name, self.address)
