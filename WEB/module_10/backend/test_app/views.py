from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from .models import Quote, Author


def index(request):
    query = Quote.objects.all()
    paginator = Paginator(query, 6)
    page = request.GET.get('page')
    quotes = paginator.get_page(page)
    return render(request, "test_app/index.html", context={"quotes": quotes})


def all_authors(request):
    authors = Author.objects.all()
    return render(request, "test_app/all_authors.html", context={"authors": authors})


def specific_author(request, fullname):
    author = Author.objects.filter(fullname=fullname).first()
    return render(request, "test_app/single_author.html", context={"author": author})
