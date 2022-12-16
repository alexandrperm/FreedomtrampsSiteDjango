import django import forms
from .models import Category


class PostForm(forms.Form):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to='photos/%Y/%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', verbose_name='Наименование категории', on_delete=models.PROTECT, null=True)
