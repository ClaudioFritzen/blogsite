from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Post

from .forms import CommentForm, PostForm

# Create your views here.

def frontpage(request):

    # buscando todos os post no banco
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts':posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

 
# função page home
def home(request):
    return render(request, 'blog/home.html')



#3 new post

def new_post(request):
    
    if request.method == "GET":

        return render(request,'blog/new_post.html')
    
    elif request.method == "POST":

        title = request.POST.get('title')
        slug = request.POST.get('slug')
        intro = request.POST.get('intro') 
        body = request.POST.get('body') 

        try:
            ## SLUG deve ser unico
            new_post = Post.objects.create(
                title=title,
                slug=slug,
                intro=intro,
                body=body
            )
            
        except:
            return HttpResponse('Falha ao conectar com o banco! tente mais tarde!')

        print(title, slug, intro, body)
    
        return HttpResponse('Metodo POST')