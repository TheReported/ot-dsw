# Generated by Django 4.2.7 on 2023-11-26 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitors', '0004_alter_competitor_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='job',
            field=models.TextField(max_length=200),
        ),
    ]
