from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)
    content = models.TextField()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
