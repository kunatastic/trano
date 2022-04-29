from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from trains.models import Train, TRAIN_TYPE_CHOICES, Coach, TRAIN_COACH_TYPE_CHOICES
from passengers.models import Passenger

# Create your views here.

class HomeView(LoginRequiredMixin, View):
    template_name = "app/routes/home.html"

    def get(self, request):
        request.full_name = request.user.get_full_name()
        return render(
            request,
            self.template_name,
            {"title": "Home | Welcome to Trano Dashboard", "page": "home"},
        )


class TrainListView(LoginRequiredMixin, ListView):
    template_name = "app/routes/trains.html"
    context_object_name = "trains"

    def get_queryset(self):
        return Train.objects.filter(
            deleted=False,
            tte=self.request.user,
            arrival__gte=datetime.now(),
        )
    
    def get_context_data(self, **kwargs):
        context = super(TrainListView, self).get_context_data(**kwargs)
        context.update({"title": "Trains | Trano Dashboard", "train_choices": TRAIN_TYPE_CHOICES})
        return context

class CoachListView(LoginRequiredMixin, ListView):
    template_name = "app/routes/coaches.html"
    context_object_name = "coaches"

    def get_queryset(self):
        return Coach.objects.filter(
            deleted=False,
            train = Train.objects.get(pk = self.kwargs.get('train_pk')),
        ).order_by("type")
    
    def get_context_data(self, **kwargs):
        context = super(CoachListView, self).get_context_data(**kwargs)
        context.update({
            "title": "Coaches | Trano Dashboard", 
            "train_choices": TRAIN_COACH_TYPE_CHOICES,
            "train": Train.objects.get(pk = self.kwargs.get('train_pk'))
            })
        return context

class PassengerListView(LoginRequiredMixin, ListView):
    template_name = "app/routes/passengers.html"
    context_object_name = "passengers"

    def get_queryset(self):
        return Passenger.objects.filter(
            train = Train.objects.get(pk = self.kwargs.get("train_pk")),
            coach = Coach.objects.get(pk = self.kwargs.get("coach_pk")),
            deleted = False,
            confirmed = True,
        ).order_by("seat_number")

    def get_context_data(self,**kwargs):
        context = super(PassengerListView, self).get_context_data(**kwargs)
        context.update({
            "title": "Passengers | Trano Dashboard",
            "train": Train.objects.get(pk = self.kwargs.get('train_pk')),
            "coach": Coach.objects.get(pk = self.kwargs.get('coach_pk')),
        })
        return context


def ModifyPassengerBoardingInfoApi(LoginRequiredMixin, request):

    def get(self, request, *args, **kwargs):
        print("GET", request.GET)
