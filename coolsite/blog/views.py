from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


from .forms import *
from .models import  *

menue = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add blog', 'url_name': 'add_page'},
    {'title': 'Feedback', 'url_name': 'contact'},
    {'title': 'Join', 'url_name': 'login'},


]

class NewsHome(ListView):
    model = News
    template_name = "blog/index.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menue
        context['title'] = "Main page"
        context['cat_selected'] = 0

        return context

    def get_queryset(self):
        return News.objects.filter(is_published = True)
# def index(request):
#     posts = News.objects.all()
#
#     context = {'posts': posts,
#                'menu': menue,
#                'title': "Main page",
#                'cat_selected':0}
#
#     return render(request, 'blog/index.html', context =context)
#

def about(request):
    return render(request, 'blog/about.html', {"menu": menue, 'title': "About site"})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'blog/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add blog"
        context['menu'] = menue
        return context
# def addpage(request)  :
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES )
#         if form.is_valid():
#             print(form.cleaned_data)
#
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     return render(request, 'blog/addpage.html', {'form': form, 'menu': menue, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse("Feedback")


def login(request):
    return HttpResponse("Join")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"Sorry page not found:(")  # Page 404


# def show_post(request, post_slug):
#     post = get_object_or_404(News, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menue,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, "blog/post.html", context=context)

class ShowPost(DetailView):
    model = News
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menue
        return context

class NewsCategory(ListView):
    model = News
    template_name = "blog/index.html"
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(cat__slug = self.kwargs['cat_slug'], is_published = True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Category -"+ str(context['posts'][0].cat)
        context['menu'] = menue
        context['cat_selected'] = context['posts'][0].cat_id

        return context

# def show_category(request, cat_id):
#     posts = News.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menue,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'blog/index.html', context=context)

# Create your views here.
