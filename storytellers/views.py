from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request, 
                 'storytellers/post/list.html' ,
                 {'posts': posts})

def post_detail(request, year, month, day, Post):
    post = get_object_or_404(Post,  slug=post,
                                    status= 'published',
                                    publish__year = year,
                                    publish_month = month,
                                    publish_day= day)
    return render(request,
                 'storytellers/post/list.html',
                 {'post': post})