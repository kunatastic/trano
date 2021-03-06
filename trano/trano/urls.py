"""trano URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from users.views import *
from application.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path("user/signin/" , UserSignInView.as_view(), name="user_signin"),
    path("user/logout/" , UserLogOutView.as_view(), name="user_logout"),

    # PLATFORM
    path("", TrainListView.as_view(), name="platform_welcome"),
    path("train/", TrainListView.as_view(), name="platform_trains"),
    path("train/<int:train_pk>/coach/", CoachListView.as_view(), name="platform_train_detail"),
    path("train/<int:train_pk>/coach/<int:coach_pk>/passenger/", PassengerListView.as_view(), name="platform_train_coach_passenger"),

    # API
    path("train/<int:train_pk>/coach/<int:coach_pk>/passenger/<int:passenger_pk>/modify/",ModifyPassengerBoardingInfoApi)
]
