from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})


def success(request):
    return render(request, "contact/success.html")


def about(request):
    return render(request, "about.html")


def events(request):
    return render(request, "events.html")


def index(request):
    return render(request, "index.html")
