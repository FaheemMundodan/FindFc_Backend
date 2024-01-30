from django.shortcuts import render
from django.http import HttpResponse
from .models import details


def index(request):

    context = {
        "events": details.objects.all()
    }
    return render(request,"events/index.html", context)

# Create your views here.
