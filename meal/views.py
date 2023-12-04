from django.shortcuts import render

from .meals import meal_categories

# Create your views here.


def meals(req):
    return render(req, "meals.html", {"meals": meal_categories})
