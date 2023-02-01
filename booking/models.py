from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Room(models.Model):
    
    room_name = models.CharField(max_length=255, blank=False, null=True)
    # Defining Room Type:
    default_answer = 0
    single = 1
    double = 2
    family = 3
    room_type = (
        (default_answer, "Default"),
        (single, "Single"),
        (double, "Double"),
        (family, "Family")
    )
    
    room_type = models.IntegerField(choices=room_type, null=False, blank=False)
    room_number = models.IntegerField(blank=False, null=False, unique=True)
    
    #Room Availability
    yes = 0
    no = 1
    is_available = (
        (yes, "YES"),
        (no, "NO")
    )
    
    available = models.IntegerField(choices=is_available, blank=False, null=False)
    
    def save(self, *args, **kwargs):
        self.room_name = self.room_type
        super(Room, self).save(*args, **kwargs)
    
    def __str__(self):
        return "{}".format(self.room_name)

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
    
    def __str__(self):
        return "{}".format(self.room)

class Customer(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(blank=True, null=False)
    phone_number = PhoneNumberField(null=False, blank=True, unique=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, blank=False, null=True)
    def __str__(self):
        return "{}".format(self.name, self.address)
    
class Guest(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(blank=True, null=False)
    phone_number = PhoneNumberField(null=False, blank=True, unique=True)
    
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=False)
    def __str__(self):
        return "{}{}".format(self.name, self.address)
