from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogs

def index(request):
    news = Blogs.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='blogs/index.html', context=context)
