from django.db import models
from django.utils.crypto import get_random_string

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_unique_short_url()
        super().save(*args, **kwargs)

    def generate_unique_short_url(self):
        short_url = get_random_string(6)
        while URL.objects.filter(short_url=short_url).exists():
            short_url = get_random_string(6)
        return short_url

    def __str__(self):
        return self.original_url
