from django.urls import path

from .views import *


urlpatterns = [
    path("", PostList.as_view(), name="news"),
    path("category/<slug:slug>/", PostList.as_view(), name="category_post"),
    path("comment/<int:pk>/", AddComment.as_view(), name="add_comment"),
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
]