from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class Section(models.Model):
    section_title = models.CharField(max_length=250)
    section_priority = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.section_title + ': ' + str(self.section_priority)


class Lesson(models.Model):
    section_key = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = RichTextUploadingField()
    author = models.CharField(max_length=20, default="admin")
    pub_date = models.DateTimeField(default=timezone.now)
    voices = models.IntegerField(default=0)
    rate = models.FloatField(default=0)


class LessonComment(models.Model):
    article = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    content = models.TextField(default="Ваш комментарий...")
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
