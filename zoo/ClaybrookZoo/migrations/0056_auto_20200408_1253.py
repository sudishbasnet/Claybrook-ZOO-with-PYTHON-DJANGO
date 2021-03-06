# Generated by Django 2.2.4 on 2020-04-08 07:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClaybrookZoo', '0055_auto_20200408_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterModelOptions(
            name='sponsor',
            options={'ordering': ('-review_date',)},
        ),
        migrations.AlterModelOptions(
            name='update',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterModelOptions(
            name='watchlist',
            options={'ordering': ('-observation_date',)},
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ManyToManyField(blank=True, related_name='message_receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('zoo keeper', 'zoo keeper'), ('manager', 'manager'), ('visitor', 'visitor'), ('temporary staff', 'temporary staff')], default='visitor', max_length=15),
        ),
    ]
