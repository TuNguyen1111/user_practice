from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm

# Create your views here.

@login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'registration/sign_up.html', context)