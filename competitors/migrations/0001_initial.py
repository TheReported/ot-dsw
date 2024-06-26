# Generated by Django 4.2.7 on 2023-11-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music_styles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('slug', models.SlugField(max_length=250)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('subject', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('job', models.CharField(max_length=80)),
                ('hobbies', models.TextField(max_length=200)),
                ('avatar', models.ImageField(blank=True, upload_to='competitors/')),
                ('music_styles', models.ManyToManyField(to='music_styles.musicstyle')),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
    ]
