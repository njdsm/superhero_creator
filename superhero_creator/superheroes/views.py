from django.shortcuts import render
from .models import Superhero
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)


def detail(request, superhero_id):
    specific_superhero = Superhero.objects.get(id=superhero_id)
    context = {
        'specific_superhero': specific_superhero
    }
    return render(request, 'superheroes/detail.html', context)


def create(request):
    if request.method == 'POST':
        superhero_name = request.POST.get('superhero_name')
        alter_ego_name = request.POST.get('alter_ego_name')
        primary_ability = request.POST.get('primary_ability')
        alternate_ability = request.POST.get('alternate_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(superhero_name=superhero_name, alter_ego_name=alter_ego_name,
                                  primary_ability=primary_ability, alternate_ability=alternate_ability,
                                  catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


def edit(request, superhero_id):
    superhero = Superhero.objects.get(id=superhero_id)
    context = {
        'superhero': superhero
    }
    if request.method == 'POST':
        superhero.superhero_name = request.POST.get('superhero_name')
        superhero.alter_ego_name = request.POST.get('alter_ego_name')
        superhero.primary_ability = request.POST.get('primary_ability')
        superhero.alternate_ability = request.POST.get('alternate_ability')
        superhero.catchphrase = request.POST.get('catchphrase')
        superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/edit.html', context)


