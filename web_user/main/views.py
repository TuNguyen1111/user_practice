from django.shortcuts import render, HttpResponse

from .forms import RegistrationForm

# Create your views here.


def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'registration/sign_up.html', context)