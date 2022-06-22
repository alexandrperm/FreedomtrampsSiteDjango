from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=150)

    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%d')
    is_published = models.BooleanField(default=True)

    #задаём дефолтное представление объекта
    def __str__(self):
        return self.title
