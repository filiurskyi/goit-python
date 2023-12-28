from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("signout/", views.sign_out, name="sign_out"),
    path("add-quote/", views.add_quote, name="add_quote"),
]
