from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required  
from app.models import Filma
from django.core.paginator import Paginator



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


