from blog.models import post
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts =[
    {
        'author': 'Rohit',
        'title': 'Blog post 1',
        'content': 'First post content ',
        'date_posted': '30 may, 2021'
    },
    {
       'author': 'Rahul',
        'title': 'Blog post 2',
        'content': '2nd post content ',
        'date_posted': '31st may, 2021'
    
    }
]



def home(request):
    context ={
        'posts': post.objects.all()
    }
    return render(request , 'blog/home.html', context)


def about(request):
    return render(request , 'blog/about.html', {'title': 'About'})