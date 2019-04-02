from django import template

from photologue.models import Gallery


register = template.Library()


@register.inclusion_tag("tags/base_tags.html")
def gallery(name, template="tags/gallery.html"):
    return {
        "template": template,
        "gallery": Gallery.objects.get(title=name)
    }


