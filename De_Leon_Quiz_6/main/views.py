from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .models import Post
from django.core.paginator import Paginator
from .forms import CustomUserCreationForm, PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'main/home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Make inactive until admin approves
            user.save()
            messages.success(request, 'Account created successfully. Please wait for admin approval.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please check the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Order posts by most recent
    return render(request, 'main/post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your post has been created.')
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form})

