from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic.base import View

from .models import Post, Category
from .forms import CommentForm


class PostList(View):
    """Список статей"""
    def get(self, request, slug=None):
        if slug is not None:
            posts = get_list_or_404(Post, category__slug=slug)
        else:
            posts = Post.objects.all()
        return render(request, 'news/post-list.html', {"posts": posts})


class PostDetail(View):
    """Вывод полной статьи"""
    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        form = CommentForm()
        return render(request, 'news/post-detail.html', {"post": post, "form": form})


class AddComment(View):
    """Добавление комментариев"""
    def post(self, request, pk):
        # text = request.POST.get("text")
        # print(text)
        form = CommentForm(request.POST)
        # text = form.changed_data["text"]
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(id=pk)
            form.save()
            return redirect("news")
        else:
            return HttpResponse(status=400)
