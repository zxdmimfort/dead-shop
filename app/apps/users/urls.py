from django.urls import path

from .views import UserCreateView, logout_view, sign_in

app_name = "users"

urlpatterns = [
    path("sign-up/", view=UserCreateView.as_view(), name="sign_up"),
    path("sign-in/", view=sign_in, name="sign_in"),
    path("sign-out/", view=logout_view, name="sign_out"),
]
