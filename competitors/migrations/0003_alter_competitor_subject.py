# Generated by Django 4.2.7 on 2023-11-26 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitors', '0002_rename_birth_date_competitor_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='subject',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]