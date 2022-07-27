from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('post/<int:posts_id>/', view_posts, name='view_posts'),

]
