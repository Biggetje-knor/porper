from django.shortcuts import render
from .models import Blog

def all_blog(request):
    blogs = Blog.objects.all()
    return render(request,'blog/all_blog.html',{'blog':blogs})



