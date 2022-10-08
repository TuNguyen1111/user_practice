from pickle import TRUE
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required

from .forms import RegistrationForm, PostForm
from .models import Post

# Create your views here.

@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        post = Post.objects.filter(id=post_id).first()
        has_permisstion_delete_post = post.author == request.user or request.user.has_perm('main.delete_post')
        if has_permisstion_delete_post:
            post.delete()

    context = {
        'posts': posts
    }
    return render(request, 'main/home.html', context)

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

@permission_required('main.add_post', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'main/create_post.html', context)
