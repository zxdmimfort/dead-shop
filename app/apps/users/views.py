from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import LoginForm, UserCreateForm
from .models import Client


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = "users/sign-up.html"
    success_url = "users:login"
    model = Client


def sign_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                print("success")
                return redirect("products:index")
            else:
                print("error")
                return render(request, "users/login.html")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("products:index")
