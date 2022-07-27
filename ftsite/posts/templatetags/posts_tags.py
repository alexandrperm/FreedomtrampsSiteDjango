from django import template
from posts.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('posts/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}
