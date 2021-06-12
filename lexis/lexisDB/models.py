from lexisDB.sound import make_speech
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image, ImageDraw
from django.core.files import File


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    image = models.ImageField(default='def.png', upload_to='profile_pics')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


class Theme(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=500, blank=True, null=True)

    Options = (
        ('A1', 'Beginner'),
        ('A2', 'PreIntermediate'),
        ('B1', 'Intermediate'),
        ('B2', 'UpperIntermediate'),
        ('C1', 'Advanced'),
        ('C2', 'Proficiency')
    )

    level = models.CharField(max_length=50, choices=Options, blank=False, default=0)


class Word(models.Model):
    content = models.CharField(max_length=100, blank=False)
    part_of_speech = models.CharField(max_length=100, blank=True)
    translation = models.CharField(max_length=100, blank=True)
    article = models.CharField(max_length=100, blank=True)
    plural = models.CharField(max_length=100, blank=True)
    context = models.CharField(max_length=100, blank=True)
    meaning = models.CharField(max_length=100, blank=True)
    queue_value = models.IntegerField(blank=True, null=True)
    queue_next_value = models.IntegerField(blank=True, null=True)

    audio = models.FileField(upload_to='audio', null=True, blank=True)

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)


@receiver(post_save, sender=Word)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        
        count = Word.objects.filter(theme=instance.theme).count()
        instance.queue_value = count
        instance.queue_next_value = count + 1
        instance.save()
        #print('DB')
        #print(words)
        make_speech(instance.translation)
        instance.audio.save('media.mp3', content=File(open('speech.mp3', 'rb')))


class Card(models.Model):

    status = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now=True, blank=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)


class Result(models.Model):
    time = models.DateTimeField(auto_now=True, blank=False)
    type = models.CharField(max_length=100, blank=True)
    score = models.FloatField(blank=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
