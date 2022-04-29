from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from trains.models import Train, Coach
from users.models import TrainTicketExaminer, Traveller
from passengers.models import Passenger

# Register your models here.
admin.site.register(TrainTicketExaminer, UserAdmin)
admin.site.register(Train)
admin.site.register(Coach)
admin.site.register(Traveller)
admin.site.register(Passenger)
