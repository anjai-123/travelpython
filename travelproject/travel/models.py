from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='picture')

    def __str__(self):
        return self.name
class Team(models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField()
    image=models.ImageField(upload_to='picture')

    def __str__(self):
        return self.name

