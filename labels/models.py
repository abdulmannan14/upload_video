from django.db import models
from django.contrib.auth.models import User
from video.models import Video
# Create your models here.

class Label_types(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Label(models.Model):
    name= models.CharField(max_length=200)
    type = models.ForeignKey(Label_types,on_delete=models.CASCADE,null=False)
    def __str__(self):
        return self.name



class User_Label(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    video= models.ForeignKey(Video,on_delete=models.CASCADE,null=False)
    lebels= models.ForeignKey(Label,on_delete=models.CASCADE,null=False)
    type = models.ForeignKey(Label_types,on_delete=models.CASCADE,null=False)
    def __str__(self):
        return self.lebels.name



