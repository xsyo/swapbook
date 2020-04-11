# Generated by Django 3.0.5 on 2020-04-08 11:43

from django.db import migrations, models
import users.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=users.utilities.get_avatar_path, verbose_name='Аватар'),
        ),
    ]