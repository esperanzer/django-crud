from django.shortcuts import render
# from django.views.generic.edit import CreateView
from .models import Post
from django.views.generic.list import ListView
# Create your views here.



class PostListView(ListView):
    model=Post