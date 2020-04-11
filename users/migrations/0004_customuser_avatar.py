# Generated by Django 3.0.5 on 2020-04-08 11:37

from django.db import migrations, models
import users.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200407_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(null=True, upload_to=users.utilities.get_avatar_path, verbose_name='Аватар'),
        ),
    ]