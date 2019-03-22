from django.urls import path

from .views import *


urlpatterns = [
    path("", PostList.as_view(), name="news"),
    path("search/", Search.as_view(), name="search_form"),
    path("<slug:category>/", PostList.as_view(), name="category_post"),
    path("<slug:category>/<slug:slug>/", PostDetail.as_view(), name="post_detail"),
]