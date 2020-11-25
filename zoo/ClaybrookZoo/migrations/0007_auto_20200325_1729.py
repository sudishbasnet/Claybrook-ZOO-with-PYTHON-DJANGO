# Generated by Django 2.2.4 on 2020-03-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClaybrookZoo', '0006_auto_20200325_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='payment_received',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=3),
        ),
    ]