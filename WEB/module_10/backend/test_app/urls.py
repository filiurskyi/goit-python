from django.urls import path

from . import views

app_name = "test_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("authors/<str:fullname>", views.specific_author, name="specific_author"),
    path("authors/", views.all_authors, name="all_authors"),
]
