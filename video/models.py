from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.
from model_utils import Choices



class Video(models.Model):
    # listi=[]
    # lista=[]
    # single_user = User.objects.all()
    # for i in single_user:
    #     if i.is_superuser == 1:
    #         pass
    #     else:
    #         a=i.username
    #         listi.append(a)
    # for i in range(len(listi)):
    #     b=(listi[i])
    #     a=(str(b), str(b))
    #     lista.append(a)
    # CHOICES = (lista)
    caption= models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    # show_to = MultiSelectField(choices=CHOICES)
    show_to = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.caption



# class User_Label(models.Model):
#     user= models.ForeignKey(User,on_delete=models.CASCADE,null=False)
#     video= models.ForeignKey(Video,on_delete=models.CASCADE,null=False)
#     lebels= models.ForeignKey(Label,on_delete=models.CASCADE,null=False)
#     def __str__(self):
#         return self.lebels.name