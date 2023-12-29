from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import LoginForm, AddQuoteForm, AddAuthorForm
from .forms import RegisterForm
from test_app.models import Quote, Author # noqa

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect(to='test_app:index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='users:login')
        else:
            return render(request, 'users/register.html', context={"form": form})

    return render(request, 'users/register.html', context={"form": RegisterForm()})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect(to='test_app:index')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')
        login(request, user)
        return redirect(to='users:dashboard')
    return render(request, 'users/login.html', context={"form": LoginForm()})


# @login_required
@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = "users/dashboard.html"
    success_url = reverse_lazy("dashboard")

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['quotes'] = Quote.objects.filter(created_by=2).all()
        context['authors'] = Author.objects.filter(created_by=2).all()
        return context


@method_decorator(login_required, name='dispatch')
class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect("test_app:index")


@method_decorator(login_required, name='dispatch')
class QuoteCreateView(CreateView):
    model = Quote
    form_class = AddQuoteForm
    template_name = "users/add_quote.html"
    success_url = reverse_lazy("users:dashboard")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class AuthorCreateView(CreateView):
    model = Author
    form_class = AddAuthorForm
    template_name = "users/add_author.html"
    success_url = reverse_lazy("users:dashboard")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


