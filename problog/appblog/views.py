from django.shortcuts import render
from .templates import*
from .models import*

# Create your views here.

def nav(request):
    return render(request,'nav.html')

from django.views.generic import ListView
class ListBlog(ListView):
    model=Post
    template_name='home.html'
    context_object_name='blg'

from django.views.generic.detail import DetailView
class DetailBlog(DetailView):
    model=Post
    template_name='detail.html'
    context_object_name='blg'

from django.views.generic import CreateView
from django.urls import reverse_lazy
class Createblog(CreateView):
    model=Post
    template_name='create.html'
    fields='__all__'
    success_url=reverse_lazy('home')


from django.views.generic import UpdateView
class Editblog(UpdateView):
    model=Post
    template_name='edit.html'
    fields='__all__'
    success_url=reverse_lazy('home')

from django.views.generic import DeleteView
class Deleteblog(DeleteView):
    model=Post
    template_name='delete.html'
    success_url=reverse_lazy('home')
