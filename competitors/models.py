from django.conf import settings
from django.db import models
from django.urls import reverse

from music_styles.models import MusicStyle


class Competitor(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACT', 'ACTIVE'
        NOMINATED = 'NOM', 'NOMINATED'
        KICKED = 'KIC', 'KICKED'

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80, blank=True)
    slug = models.SlugField(max_length=250)
    birthdate = models.DateField(blank=True, null=True)
    subject = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=80)
    job = models.TextField(max_length=200)
    hobbies = models.TextField(max_length=200)
    avatar = models.ImageField(upload_to='competitors/', blank=True)
    music_styles = models.ManyToManyField(MusicStyle)
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        ordering = ['first_name']

    @property
    def get_avatar(self):
        if not self.avatar:
            return f'{settings.STATIC_URL}img/default_avatar.png'
        return self.avatar

    def get_absolute_url(self):
        return reverse("competitors:detail", args=[self.slug])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
