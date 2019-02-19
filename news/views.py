from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.base import View

from .models import Post, Category


class PostList(View):
    """Список статей"""
    def get(self, request):
        posts = Post.objects.filter(category_id=1)

        print(posts)
        # if posts.exists():
        #     return HttpResponse(posts)
        # else:
        #     raise Http404
        # for post in posts:
        #     print(post)
        return HttpResponse(posts)
