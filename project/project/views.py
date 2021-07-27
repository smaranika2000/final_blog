from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import Post






def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "blogPost.html", context)
