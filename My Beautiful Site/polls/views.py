from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    x = ""
    for i in range(10000):
        x = x + "I strongly dislike Django with a burning a passion "
    return HttpResponse(x)
