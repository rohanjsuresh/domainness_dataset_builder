from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Keywords_in_Circulation(models.Model):
    keyword = models.CharField(max_length=512)
    times_classified = models.IntegerField(default=0)
    times_skipped = models.IntegerField(default=0)

class Keywords_Classified(models.Model):
    keyword = models.CharField(max_length=512)
    times_classified = models.IntegerField(default=0)
    times_skipped = models.IntegerField(default=0)

class Keywords_Skipped(models.Model):
    keyword = models.CharField(max_length=512)
    times_classified = models.IntegerField(default=0)
    times_skipped = models.IntegerField(default=0)


class Keyword_Pairs(models.Model):
    keyword_pair = models.CharField(max_length=512)
    times_classified = models.IntegerField(default=0)