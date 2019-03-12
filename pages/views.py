from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import Page


class PageView(View):
    """Вывод страницы"""
    def get(self, request, page=None):
        if page is None:
            one_page = get_object_or_404(Page, slug__isnull=True)
        else:
            one_page = get_object_or_404(Page, slug=page)
        return render(request, one_page.template, {"page": one_page})

