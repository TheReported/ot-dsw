# Generated by Django 4.2.7 on 2023-11-29 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competitors', '0006_competitor_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voted_at', models.DateTimeField(auto_now_add=True)),
                ('competitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='competitors.competitor')),
            ],
        ),
    ]
