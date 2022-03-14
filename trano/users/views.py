from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms



"""
    @url: /user/signin/
    public: True
"""

class UserSignInForm(AuthenticationForm):

    common_style = 'bg-slate-100 my-2 w-full px-4 py-2 rounded-lg text-gray-900'

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
        model = User
        fields = ['username', 'password']


class UserSignInView(LoginView):
    template_name = 'auth/signin.html'
    redirect_authenticated_user = True
    form_class = UserSignInForm
    success_url = '/'


"""
    @url: /user/signup/
    public: True
"""

class UserSignupFrom(UserCreationForm):

    common_style = 'bg-slate-100 my-2 w-full px-4 py-2 rounded-lg text-gray-900'

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': common_style,
            }
        ),
        required=True,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': common_style,
            }
        ),
        required=True,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': common_style,
            }
        ),
        required=True,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': common_style,
            }
        ),
        required=True,
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': common_style,
            }
        ),
        required=True,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': common_style,
            }
        ),
        required=True,
    )


    class Meta: 
        model = User
        fields = ["username", "password1", "password2", "email", "first_name", "last_name"]

class UserSignUpView(CreateView):
    template_name = 'auth/signup.html'
    redirect_authenticated_user = True
    form_class = UserSignupFrom
    success_url = '/'


"""
    @url: /user/signout/
    public: True
"""

class UserLogOutView(LogoutView):
    pass