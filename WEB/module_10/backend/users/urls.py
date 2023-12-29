from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.sign_in, name="login"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("signout/", views.SignOutView.as_view(), name="sign_out"),

    path("add-quote/", views.QuoteCreateView.as_view(), name="add_quote"),
    path("add-author/", views.AuthorCreateView.as_view(), name="add_author"),
    path("edit-quote/<pk>", views.QuoteUpdateView.as_view(), name="edit_quote"),
    # path("edit-author/<pk>", views., name="edit_author"),
    path("delete-quote/<pk>", views.QuoteDeleteView.as_view(), name="delete_quote"),
    # path("delete-author/<pk>", views., name="delete_author"),
]
