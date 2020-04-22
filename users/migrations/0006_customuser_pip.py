# Generated by Django 3.0.5 on 2020-04-22 08:10

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200408_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='pip',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Номер телефона'),
        ),
    ]
