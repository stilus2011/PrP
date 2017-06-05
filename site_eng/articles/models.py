from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextUploadingField()
    author = models.CharField(max_length=20, default="admin")
    pub_date = models.DateTimeField(default=timezone.now)
    voices = models.IntegerField(default=0)
    rate = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    content = models.TextField(default="Ваш комментарий...")
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:200]