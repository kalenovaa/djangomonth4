from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=500)
    producer = models.CharField(max_length=100, verbose_name='продюссер')
    rating = models.PositiveIntegerField(default=0)
    durarition = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


