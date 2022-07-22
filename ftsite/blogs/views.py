from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogs, Category


def index(request):
    news = Blogs.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',

    }
    return render(request, template_name='blogs/index.html', context=context)


def get_category(request, category_id):
    news = Blogs.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'blogs/categories.html', {'news': news, 'category': category })
