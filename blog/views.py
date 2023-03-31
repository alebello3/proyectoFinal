from django.shortcuts import render
from blog.models import post, categoria



# Create your views here.

def blog(request):
    posts= post.objects.all()
    return render(request, "blog/blog.html",{"posts":posts})

def categoria(request,categoria_id):

    categoria=categoria.objects.get(id=categoria_id)
    posts = post.objects.filter(categoria=categoria)
    return render(request, "blog/categoria.html",{'categoria':categoria, "posts":posts})
