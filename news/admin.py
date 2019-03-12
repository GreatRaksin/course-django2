from django import forms
from django.contrib import admin

from .models import Post, Category, Tag, Comment


admin.site.site_title = "Course Django"
admin.site.site_header = "Course Django"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    prepopulated_fields = {'slug': ('name',)}


class CommentAdmin(admin.TabularInline):
    """Комментарии"""
    model = Comment
    extra = 1
    # min_num = 2
    # max_num = 10
    template = 'admin/news/news.html'
    # verbose_name = "Xa-xa"
    list_display = ("id", "post", "moderation")
    list_editable = ("moderation",)


class PostProxyAdmin(admin.StackedInline):
    """Прокси модель"""
    model = Post
    extra = 3


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Статьи"""
    model = Post
    prepopulated_fields = {'slug': ('title',)}
    # inlines = [PostProxyAdmin]
    # list_display = ("id", "title", "created")
    # list_display_links = ("title",)
    # search_fields = ("title", )
    # list_filter = ("created", "category")
    # list_per_page = 1
    # list_editable = ("title",)
    # inlines = [CommentAdmin]
    # fieldsets = (
    #     (None, {
    #         "fields": (
    #             'title',
    #             'text',
    #         )
    #     }),
    #     ("Категори/Теги", {
    #         'classes': ('collapse',),
    #         "fields": (
    #             'category',
    #             'tags',
    #         )
    #     }),
    # )
    # filter_vertical = ("tags",)
    # filter_horizontal = ("tags",)
    # readonly_fields = ("viewed",)
    # prepopulated_fields = {}

    # fields = ("title",)
    # exclude = ("title", )
    # raw_id_fields = ("tags",)
    # actions_on_top = False
    # actions_on_bottom = True
    # show_full_result_count = False


# admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
# admin.site.register(Post, PostAdmin)
admin.site.register(Comment)