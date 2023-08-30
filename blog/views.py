from django.shortcuts import render

from django.http import HttpResponse

from .models import Post

# Create your views here.

def frontpage(request):

    # buscando todos os post no banco
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts':posts})

def post_detail(request, slug):

    post = Post.objects.get(slug=slug)
    return render(request,'blog/post_detail.html', {'post':post})
    

