# Generated by Django 4.2.7 on 2023-11-29 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_styles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicstyle',
            name='name',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
