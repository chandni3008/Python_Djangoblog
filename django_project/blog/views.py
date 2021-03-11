from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Person1',
        'title': 'Post1',
        'content': 'First post',
        'date_posted': 'January 1, 2021'
    },
    {
        'author': 'Person2',
        'title': 'Post2',
        'content': 'Second post',
        'date_posted': 'January 2, 2021'
    }

]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
