from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request) -> HttpResponse:
    return HttpResponse("<html><title>To-Do list</title></html>")
