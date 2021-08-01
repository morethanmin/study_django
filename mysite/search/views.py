from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.

class PublicPostIndexView(generic.ListView) :
  model = Post
  queryset = Post.objects.filter(is_public=True)

