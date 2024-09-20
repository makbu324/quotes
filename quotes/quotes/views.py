from django.shortcuts import redirect, render
from django.http import HttpResponse
from random import randrange


images = ["../static/john-lennon-the-beatles.gif", "../static/john-lennon-eyebrows.gif", "../static/john-lennon-funny.gif"]
quotes = ["\"Everything will be okay in the end. If it's not okay, it's not the end.\"", "\"Reality leaves a lot to the imagination.\"", "\"A dream you dream alone is only a dream. A dream you dream together is reality.\""]

def quote(request):
    i = randrange(3)

    context = {
        "image_link": images[i],
        "quote": quotes[i],
        "person": "John Lennon",
    }
    return render(request, "quote.html", context)

def show_all(request):
    context = {
        "images": images,
        "quotes": quotes
    }
    return render(request, "show_all.html", context)

def about(request):
    context = {
       
    }
    return render(request, "about.html", context)
