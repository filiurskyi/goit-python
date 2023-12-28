from django.shortcuts import redirect, render

# Create your views here.


def register(request):
    return render(request, "users/register.html", context={"author": "none"})


def login(request):
    return render(request, "users/login.html", context={"author": "none"})


def dashboard(request):
    return render(request, "users/dashboard.html", context={"author": "nones"})


def sign_out():
    # logout logic
    return redirect(to="/")


def add_quote(request):
    return render(request, "users/add_quote.html", context={"author": "nones"})
