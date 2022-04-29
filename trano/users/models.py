from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin

"""
    This file contains the models for the TTE & Travellers
"""


class TrainTicketExaminer(AbstractUser, PermissionsMixin):

    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=14)

    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def delete(self,*args, **kwargs):
        self.deleted = True
        self.save()

    def __str__(self):
        return f"{self.username} - {self.first_name} {self.last_name} ({self.age})"






class Traveller(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=14)

    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.age} - {self.phone}"

    def delete(self,*args, **kwargs):
        self.deleted = True
        self.save()
