from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from users.models import TrainTicketExaminer

"""
    @url: /user/signin/
    public: True
"""

class UserSignInForm(AuthenticationForm):

    common_style = "w-full py-1 px-2 outline-none"

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': common_style,
            }
        ),
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': common_style,
            }
        ),
        required=True,
    )
    class Meta: 
        model = TrainTicketExaminer
        fields = ['username', 'password']


class UserSignInView(LoginView):
    template_name = 'auth/signin.html'
    redirect_authenticated_user = True
    form_class = UserSignInForm
    success_url = '/'

"""
    @url: /user/signout/
    public: True
"""

class UserLogOutView(LogoutView):
    pass
