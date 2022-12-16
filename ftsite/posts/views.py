from django.shortcuts import render, get_object_or_404
from .models import Posts, Category


def index(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts,
        'title': 'Список новостей',

    }
    return render(request, template_name='posts/index.html', context=context)


def get_category(request, category_id):
    posts = Posts.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'posts/categories.html', {'posts': posts, 'category': category })


def view_posts(request,posts_id):
    #posts_item = Posts.objects.get(pk=posts_id)
    posts_item = get_object_or_404(Posts, pk=posts_id)
    return render(request, 'posts/view_posts.html', {"posts_item": posts_item})


def add_posts(request):
    return render(request, 'posts/add_posts.html')
