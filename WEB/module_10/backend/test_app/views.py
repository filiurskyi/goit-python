from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from .models import Author, Quote, Tag


def index(request):
    query = Quote.objects.all()
    paginator = Paginator(query, 6)
    page = request.GET.get(
        "page"
    )  # Get the current page number from the request's GET parameters
    quotes = paginator.get_page(page)
    return render(request, "test_app/index.html", context={"quotes": quotes})


def all_authors(request):
    authors = Author.objects.all().order_by("fullname")
    return render(request, "test_app/all_authors.html", context={"authors": authors})


def specific_author(request, fullname):
    author = Author.objects.filter(fullname=fullname).first()
    return render(request, "test_app/single_author.html", context={"author": author})


def all_tags(request):
    tags = Tag.objects.all().order_by("word")
    return render(request, "test_app/all_tags.html", context={"tags": tags})


def specific_tag(request, tagname):
    quotes = Quote.objects.filter(tags__word=tagname).all()
    return render(request, "test_app/specific_tag.html", context={"quotes": quotes})
