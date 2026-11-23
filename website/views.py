from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def http_test(request):
#     return HttpResponse("<h1>This is a Test</h1>")


# def json_test(request):
#     return JsonResponse({"name": "ali"})


def index_view(request):
    return render(request, "website/index.html")


def about_view(request):
    return render(request, "website/about.html")


def contact_view(request):
    return render(request, "website/contact.html")
