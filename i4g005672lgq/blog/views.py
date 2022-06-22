from statistics import mode
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView


# Create your views here.



class PostListView(ListView):
    model=Post

class PostCreateView(CreateView):
    model = Post
    field ="__all__"
    success_url = reverse_lazy("blog:all")

class DetailtView(DetailView):
    model=Post

class PostUpdateView(UpdateView):


