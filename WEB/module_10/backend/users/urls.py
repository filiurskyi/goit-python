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
    path("add-tag/", views.TagCreateView.as_view(), name="add_tag"),
    path("edit-quote/<pk>", views.QuoteUpdateView.as_view(), name="edit_quote"),
    path("delete-quote/<pk>", views.QuoteDeleteView.as_view(), name="delete_quote"),
    path("edit-author/<pk>", views.AuthorUpdateView.as_view(), name="edit_author"),
    path("delete-author/<pk>", views.AuthorDeleteView.as_view(), name="delete_author"),
    path("edit-tag/<pk>", views.TagUpdateView.as_view(), name="edit_tag"),
    path("delete-tag/<pk>", views.TagDeleteView.as_view(), name="delete_tag"),
]
