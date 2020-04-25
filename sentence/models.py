from django.db import models
from django.contrib.auth import get_user_model

from book.models import Book


class Sentence(models.Model):
    who_offers = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, 
                                    null=True, related_name='my_offers', verbose_name='Предлагатель')
    books_of_interest_1 = models.ManyToManyField(Book, verbose_name='Интересующие книги предлагателя')
    whomever_is_offered = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                                    null=True, related_name='offers', verbose_name='Получатель предложения')
    books_of_interest_2 = models.ManyToManyField(Book, blank=True, related_name='interest',
                                    verbose_name='Интересующие книги получатель предложения',
                                    db_table='BooksOfInterestToTheOfferRecipient')
    message_1 = models.TextField(default='', blank=True, verbose_name='Сообщение предлагателя') 
    reason_for_refusal = models.TextField(default='',blank=True, verbose_name='Сообщение с причиной отказа')   
    permission = models.BooleanField(default=None, null=True, verbose_name='Согласие')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    
    def __str__(slef):
        return f'Предложение ({who_offers} => {whomever_is_offered})'


    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'
        ordering = ('-created_at', '-updated_at')

