from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blog(request):
    blog = Blog.objects.all()
    return render(request,'blog/all_blog.html',{'blog':blog})

def detail(request, blog_id):
    blogs = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blogs})




