from django.db import models

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Places(models.Model):    
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    place = models.CharField(max_length=50)
    Image = models.ImageField(null=True, blank=True, upload_to="static/image")
    Description = models.TextField(max_length=500)

    def __str__(self):
        return self.place

