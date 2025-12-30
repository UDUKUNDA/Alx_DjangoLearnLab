from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'blog/base.html')

def posts(request):
    posts = Post.objects.all()
    # For now just return a simple response or we could create a template
    return HttpResponse("Here are the posts")

def login_view(request):
    return HttpResponse("Login Page")

def register(request):
    return HttpResponse("Register Page")
