from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Post, Category, Comment
from .forms import CommentForm


class PostList(ListView):
    """Список статей"""
    context_object_name = 'posts'

    def get_queryset(self):
        if self.kwargs.get('category') is not None:
            post_list = Post.objects.filter(
                category__slug=self.kwargs.get('category'),
                published=True,
                published_date__lte=datetime.now(),
            )
            if self.request.user.is_authenticated:
                posts = post_list
            else:
                posts = post_list.filter(status=False)

            if posts.exists():
                self.paginate_by = posts.first().category.pagination
                self.template_name = posts.first().category.template
        else:
            posts = Post.objects.all()
            self.paginate_by = 2
            self.template_name = 'news/post-list.html'
        return posts
        # else:
        #     raise Http404


class PostDetail(DetailView):
    """Вывод полной статьи"""
    model = Post
    template_name = 'news/post-detail.html'

    # def get_queryset(self):
    #     post = Post.objects.get(
    #             slug=self.kwargs.get('slug'),
    #             published=True,
    #             published_date__lte=datetime.now(),
    #         )
    #     return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, category, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=slug)
            form.save()
            return HttpResponseRedirect(reverse('post_detail', kwargs={"category": category, "slug": slug}))
        else:
            return HttpResponse(status=400)


class Search(View):
    """Поиск по статья и ктегориям"""
    def get(self, request):
        search = request.GET.get("search", None)
        context = Post.objects.filter(Q(title__icontains=search) |
                                      Q(category__name__icontains=search))
        # if not context.exists():
        #     context = Post.objects.filter(category__name__icontains=search)
        return render(request, 'news/post-list.html', {"posts": context})


class CategoryPost(ListView):
    """"""
    template_name = "shop/list-product.html"
    paginate_by = 5

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        node = Category.objects.get(slug=slug)
        if Post.objects.filter(category__slug=slug).exists():
            posts = Post.objects.filter(category__slug=slug)
        else:
            posts = Post.objects.filter(category__slug__in=[x.slug for x in node.get_family()])
        return posts







