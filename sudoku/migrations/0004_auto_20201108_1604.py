# Generated by Django 3.1 on 2020-11-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0003_auto_20201108_0633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranking',
            name='time',
        ),
        migrations.AddField(
            model_name='ranking',
            name='minutes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ranking',
            name='seconds',
            field=models.IntegerField(default=0),
        ),
    ]
