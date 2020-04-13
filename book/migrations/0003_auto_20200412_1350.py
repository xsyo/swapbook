# Generated by Django 3.0.5 on 2020-04-12 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_section'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('name',), 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='bookauthor',
            options={'ordering': ('name',), 'verbose_name': 'Имя автора книги', 'verbose_name_plural': 'Имена авторов книг'},
        ),
        migrations.AlterModelOptions(
            name='bookname',
            options={'ordering': ('name',), 'verbose_name': 'Имя книги', 'verbose_name_plural': 'Имена книг'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ('name',), 'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]
