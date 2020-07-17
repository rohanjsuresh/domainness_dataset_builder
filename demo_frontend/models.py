from django.db import models
from django.contrib.auth.models import User

# create table keywords( id INT NOT NULL AUTO_INCREMENT, keyword VARCHAR(512) NOT NULL, times_classified INT NOT NULL, computer_science INT NOT NULL, mathematics INT NOT NULL, physics INT NOT NULL, astronomy INT NOT NULL, electrical_engineering INT NOT NULL, quantitative_biology INT NOT NULL, statistics INT NOT NULL,  economics INT NOT NULL, other INT NOT NULL, PRIMARY KEY (id) );
class Keywords(models.Model):
    keyword = models.CharField(max_length=512)
    times_classified = models.IntegerField(default=0)
    computer_science = models.IntegerField(default=0)
    mathematics = models.IntegerField(default=0)   
    physics = models.IntegerField(default=0)
    astronomy = models.IntegerField(default=0)
    electrical_engineering = models.IntegerField(default=0)
    quantitative_biology = models.IntegerField(default=0)
    statistics = models.IntegerField(default=0)
    economics = models.IntegerField(default=0)
    other = models.IntegerField(default=0)

def __str__(self):
    return self.word

class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_done = models.IntegerField()