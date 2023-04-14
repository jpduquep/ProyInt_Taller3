from django.shortcuts import render
from .models import actor

def actors(request):
    acts = actor.objects.all()
    return render(request, 'actors.html', {'actors': acts})

