from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=259)

    def __str__(self) -> str:
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=259, unique=True)
    description = RichTextField()
    duration = models.CharField(max_length=259)
    created_at = models.TimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=259)
    description = RichTextField()
    subject = models.ForeignKey(
        Subject, related_name='topics', on_delete=CASCADE)
    duration = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title


class Link(models.Model):
    title = models.CharField(max_length=259)
    url = models.URLField(max_length=500)
    topic = models.ForeignKey(Topic, related_name='links', on_delete=CASCADE)

    def __str__(self) -> str:
        return self.title
