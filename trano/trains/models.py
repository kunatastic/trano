from django.db import models
from users.models import TrainTicketExaminer

"""
    This file contains the models for the train 
"""

TRAIN_TYPE_CHOICES = (
    ('SF', 'Super Fast Train'),
    ('F', 'Fast Train'),
    ('L', 'Local Train'),
)

class Train(models.Model):
    tte = models.ForeignKey(TrainTicketExaminer, on_delete=models.CASCADE, null=True, blank=True)

    number = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=TRAIN_TYPE_CHOICES, default='L')
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    arrival = models.DateTimeField()
    departure = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.number} - {self.name}"

    def delete(self,*args, **kwargs):
        self.deleted = True
        self.save()

TRAIN_COACH_TYPE_CHOICES = (
    ('1AC', '1AC Class'),
    ('2AC', '2AC Class'),
    ('3AC', '3AC Class'),
    ('SL', 'Sleeper'),
    ('2S', '2S Class'),
    ('GEN', 'General'),
)

class Coach(models.Model):

    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    # passengers = models.ManyToManyField(Passenger)

    total_seats = models.IntegerField()
    available_seats = models.IntegerField()
    type = models.CharField(max_length=4, choices=TRAIN_COACH_TYPE_CHOICES, default='GEN')
    number = models.CharField(max_length=10, default="GEN")

    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.train.number} [{self.type}] {self.available_seats}{self.total_seats}"

    def delete(self,*args, **kwargs):
        self.deleted = True
        self.save()

