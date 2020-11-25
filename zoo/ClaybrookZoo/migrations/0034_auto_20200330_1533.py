# Generated by Django 2.2.4 on 2020-03-30 09:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClaybrookZoo', '0033_auto_20200330_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='animal',
            field=models.ManyToManyField(blank=True, null=True, related_name='sponsored_animal', to='ClaybrookZoo.Animal'),
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='sponsored_user',
        ),
        migrations.AddField(
            model_name='sponsor',
            name='sponsored_user',
            field=models.ManyToManyField(blank=True, null=True, related_name='sponsored_user', to=settings.AUTH_USER_MODEL),
        ),
    ]