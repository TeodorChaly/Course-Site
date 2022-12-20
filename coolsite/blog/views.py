from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import  *

menue = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add blog', 'url_name': 'add_page'},
    {'title': 'Feedback', 'url_name': 'contact'},
    {'title': 'Join', 'url_name': 'login'},


]


def index(request):
    posts = News.objects.all()

    context = {'posts': posts,
               'menu': menue,
               'title': "Main page",
               'cat_selected':0}

    return render(request, 'blog/index.html', context =context)


def about(request):
    return render(request, 'blog/about.html', {"menu": menue, 'title': "About site"})


def addpage(request)  :
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                News.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')

    else:
        form = AddPostForm()

    return render(request, 'blog/addpage.html', {'form': form, 'menu': menue, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse("Feedback")


def login(request):
    return HttpResponse("Join")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"Sorry page not found:(")  # Page 404

def show_post(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'post': post,
        'menu': menue,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, "blog/post.html", context=context)

def show_category(request, cat_id):
    posts = News.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menue,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'blog/index.html', context=context)

# Create your views here.
