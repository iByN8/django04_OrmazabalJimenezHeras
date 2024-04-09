from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required  
from app.models import Filma,Bozkatzailea
from django.core.paginator import Paginator
from django.contrib import messages




def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )
@login_required
def logged(request):
    return render(request, 'app/logged.html')
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

def filmakikusi(request):
    filmak_list = Filma.objects.all()  
    paginator = Paginator(filmak_list, 5) 

    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number) 

    return render(request, 'app/filmakikusi.html', {'page_obj': page_obj})

@login_required
def bozkatu(request):
    filmak = Filma.objects.all()

    if request.method == 'POST':
        pelicula_id = request.POST.get('pelicula_id')
        pelicula = Filma.objects.get(pk=pelicula_id)
        pelicula.bozkak += 1
        pelicula.save()
        if request.user.is_authenticated:
            bozkatzailea, created = Bozkatzailea.objects.get_or_create(erabiltzailea=request.user)
            bozkatzailea.gogoko_filmak.add(pelicula)
        messages.success(request, 'Filma bozkatu da!')

    return render(request, 'app/bozkatu.html', {'filmak': filmak, 'messages': messages.get_messages(request)})



