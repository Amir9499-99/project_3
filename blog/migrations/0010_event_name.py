# Generated by Django 3.0.2 on 2020-03-27 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200326_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='Party Time!!!', max_length=150),
        ),
    ]