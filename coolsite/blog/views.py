from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import  *

menue = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add blog', 'url_name': 'add_page'},
    {'title': 'Feedback', 'url_name': 'contact'},
    {'title': 'Join', 'url_name': 'login'},


]


def index(request):
    posts = News.objects.all()
    cats = Category.objects.all()

    context = {'posts': posts,
               'cats': cats,
               'menu': menue,
               'title': "Main page",
               'cat_selected':0}

    return render(request, 'blog/index.html', context =context)


def about(request):
    return render(request, 'blog/about.html', {"menu": menue, 'title': "About site"})


def addpage(request)  :
    return HttpResponse("Add blog")


def contact(request):
    return HttpResponse("Feedback")


def login(request):
    return HttpResponse("Join")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"Sorry page not found:(")  # Page 404

def show_post(request, post_id):
    return HttpResponse(f"News about = {post_id}")

def show_category(request, cat_id):
    posts = News.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menue,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'blog/index.html', context=context)

# Create your views here.
