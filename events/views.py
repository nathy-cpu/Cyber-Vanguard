from django.shortcuts import render

# Create your views here.


def events(requests):
    return render(requests, "events/events.html")
