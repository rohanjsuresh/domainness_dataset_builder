from django.db import models
from django.contrib.auth.models import User


class Keyword(models.Model):
    word = models.CharField(max_length=100)
    belongs_to_cs = models.BooleanField(default=False)
    belongs_to_physics = models.BooleanField(default=False)
    belongs_to_math = models.BooleanField(default=False)
    belongs_to_bio = models.BooleanField(default=False)
    belongs_to_chem = models.BooleanField(default=False)
    belongs_to_hist = models.BooleanField(default=False)
    belongs_to_stop = models.BooleanField(default=False)
    belongs_to_other = models.BooleanField(default=False)    

    def __str__(self):
        return self.word

class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_done = models.IntegerField()