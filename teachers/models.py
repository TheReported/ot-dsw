from django.conf import settings
from django.db import models
from django.urls import reverse


class Teacher(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=250)
    subject = models.CharField(max_length=80)
    avatar = models.ImageField(upload_to='teachers/', blank=True)

    class Meta:
        ordering = ['first_name']

    @property
    def get_avatar(self):
        if not self.avatar:
            return f'{settings.STATIC_URL}img/default_avatar.png'
        return self.avatar

    def get_absolute_url(self):
        return reverse("teachers:detail", args=[self.slug])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
