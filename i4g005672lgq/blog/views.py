from statistics import mode
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Post
from django.views.generic.list import ListView
# Create your views here.



class PostListView(ListView):
    model=Post

class PostCreateView(CreateView):
    model = Post
    field ="__all__"
    success_url = reverse_lazy("blog:all")


