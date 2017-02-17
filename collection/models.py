from django.contrib.auth.models import User
from django.db import models

class Verse(models.Model):
  ref = models.CharField(max_length=255)
  text = models.TextField()
  version = models.CharField(max_length=16)
  slug = models.SlugField(unique=True)
  user = models.OneToOneField(User, blank=True, null=True)