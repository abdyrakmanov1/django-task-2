from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    book = models.FileField(upload_to='books/files/')
    image = models.ImageField(upload_to='images/covers/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
