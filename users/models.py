from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from .utilities import get_avatar_path

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'



class CustomUser(AbstractUser):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, verbose_name='Город')
    avatar = models.ImageField(verbose_name='Аватар', upload_to=get_avatar_path, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('users:user_detail', args=[str(self.pk)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



