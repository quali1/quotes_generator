from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=30)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ["tag"]


class Quote(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=100, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    hide_creator = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    likes_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
