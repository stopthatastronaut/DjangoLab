from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def home_view(request, *args, **kwargs):
    today = datetime.now()
    template = loader.get_template("home.html")
    context = {
        'todays_date': today}

    return HttpResponse(template.render(context, request))
