from django.db import models
from trains.models import Train, Coach
from users.models import Traveller

# Create your models here.
class Passenger(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    traveller = models.ForeignKey(Traveller, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)

    seat_number = models.IntegerField()
    confirmed = models.BooleanField(default=False)
    waitingList = models.IntegerField(default=-1)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    boarded = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.train.number} - {self.coach.type} - {self.seat_number}"

    def delete(self,*args, **kwargs):
        self.deleted = True
        self.save()

