from django.shortcuts import render

from .models import Post

# Create your views here.

def frontpage(request):

    # buscando todos os post no banco
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts':posts})