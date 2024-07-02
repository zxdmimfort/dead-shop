from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import CreateView

from .forms import LoginForm, UserCreateForm
from .models import Client


class UserCreateView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("products:index")
    model = Client

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return JsonResponse({"success": True})

    def form_invalid(self, form):
        return JsonResponse({"success": False, "errors": form.errors})


def sign_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False, "error": "Invalid email or password"})
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = LoginForm()
    return JsonResponse({"success": False, "error": "Invalid request method"})


def logout_view(request):
    logout(request)
    return redirect("products:index")

def index(request):
    login_form = LoginForm()
    register_form = UserCreateForm()
    return render(request, 'base.html', {'login_form': login_form, 'register_form': register_form})