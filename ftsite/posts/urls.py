from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('', index, name='posts'),
    path('', index, name='about'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('post/<int:posts_id>/', view_posts, name='view_posts'),
    path('post/add-post/', add_posts, name='add_posts'),
]
