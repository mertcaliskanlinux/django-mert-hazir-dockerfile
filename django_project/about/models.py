from django.db import models


# Create your models here.
class About(models.Model):

    title = models.CharField(max_length=140,blank=True,null=True)
    image_one = models.ImageField(upload_to='about/',blank=True,null=True)
    image_two = models.ImageField(upload_to='about/',blank=True,null=True)
    image_three = models.ImageField(upload_to='about/',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    subtitle_one = models.CharField(max_length=140,blank=True,null=True)
    subtitle_one_desc = models.TextField(blank=True,null=True)
    subtitle_two = models.CharField(max_length=140,blank=True,null=True)
    subtitle_two_desc = models.TextField(blank=True,null=True)
    
    
    def __str__(self):
        return self.title