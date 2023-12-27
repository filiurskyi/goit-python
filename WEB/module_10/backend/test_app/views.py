from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def index(request):
    return render(request, "test_app/index.html", context={"msg": "Testing msg context!"})
