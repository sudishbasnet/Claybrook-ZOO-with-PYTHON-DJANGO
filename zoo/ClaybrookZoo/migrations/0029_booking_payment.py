# Generated by Django 2.2.4 on 2020-03-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClaybrookZoo', '0028_auto_20200329_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=10),
        ),
    ]
