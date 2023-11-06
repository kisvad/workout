from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Routine(models.Model):
    title = models.CharField(max_length=255, null=False)
    slug = models.SlugField(max_length=255, null=False, unique=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("routine_detail", kwargs={"pk": self.pk, "slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)