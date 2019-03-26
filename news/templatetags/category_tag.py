from django import template

from news.models import Category


register = template.Library()


@register.inclusion_tag("tags/base_tags.html")
def category_list(template="tags/category-list.html"):
    return {
        "template": template,
        "list_category": Category.objects.all()
    }


