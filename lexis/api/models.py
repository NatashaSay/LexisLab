from django.db import models
from textblob import TextBlob
from django.conf import settings


class Themes(models.Model):
    options = (
        ('other', 'other'),
        ('beginner', 'A1'),
        ('preintermediate', 'A2'),
        ('intermediate', 'B1'),
        ('upperintermediate', 'B2'),
        ('advanced', 'C1'),
    )

    title = models.TextField(max_length=20)
    level = models.CharField(max_length=20, choices=options, default='beginner')
    description = models.TextField(max_length=150)

    def __str__(self):
        return self.title


class Words(models.Model):
    theme = models.ForeignKey(Themes, on_delete=models.PROTECT, default=1)
    content = models.TextField()
    part_of_speech = models.TextField(default='unknown')
    translation = models.TextField()
    article = models.TextField(blank=True)
    plural = models.TextField(blank=True)
    context = models.TextField(blank=True)
    meaning = models.TextField(blank=True)
    meaning1 = models.TextField(blank=True)
    meaning1 = models.TextField(blank=True)


    def translate(self):
        
        blob = TextBlob(self.content)
        self.translation = blob.translate(to='de').string
        return self.translation