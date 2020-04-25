from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from .utilities.path_generator import book_image_path


class BookName(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя книги')

    wishful = models.ManyToManyField(get_user_model(), related_name='desired_books', verbose_name='Желатели книги')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book:book_name_detail', args=[self.pk])
    
    class Meta:
        verbose_name = 'Имя книги'
        verbose_name_plural = 'Имена книг' 
        ordering = ('name',)

class BookAuthor(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя автора')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Имя автора книги'
        verbose_name_plural = 'Имена авторов книг' 
        ordering = ('name',)

class Section(models.Model):
    name = models.CharField(max_length=250, verbose_name='Раздел')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы' 
        ordering = ('name',)

class Book(models.Model):
    name = models.ForeignKey(BookName, on_delete=models.CASCADE, related_name='books', verbose_name='Название')
    author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE, related_name='author_books', verbose_name='Автор')
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL, related_name='section_books', verbose_name='Раздел')
    year_of_publishing = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Год издания')
    isbn = models.CharField(unique=True, max_length=25, verbose_name='ISBN')
    publisging_house = models.CharField(max_length=50, verbose_name='Издательство', blank=True, null=True)
    page_count = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество страниц')
    img = models.ImageField(upload_to=book_image_path, verbose_name='Обложка книги', blank=True, null=True)
    slug = models.SlugField(db_index=True)

    holders = models.ManyToManyField(get_user_model(), related_name='my_books', verbose_name='Обладатели книги')

    def __str__(self):
        return f'{self.name.name} - {self.author.name}'

    def get_absolute_url(self):
        return reverse('book:book_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги' 
        ordering = ('name', 'author')
    




