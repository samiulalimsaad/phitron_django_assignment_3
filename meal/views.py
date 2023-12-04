from django.shortcuts import render

# Create your views here.


def meals(req):
    return render(req, "home.html")
