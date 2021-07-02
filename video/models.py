from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.


class User_Videos(models.Model):
    listi=[]
    lista=[]
    single_user = User.objects.all()
    for i in single_user:
        if i.is_superuser == 1:
            pass
        else:
            a=i.username
            print("this is a",a)
            listi.append(a)
    print("this is list" ,listi)


    for i in range(len(listi)):
        b=(listi[i])
        a=(str(b), str(b))
        lista.append(a)

    print('this is lista',lista)
    YEAR_IN_SCHOOL_CHOICES = (lista)
    caption= models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    show_to = MultiSelectField(choices=YEAR_IN_SCHOOL_CHOICES)
    def __str__(self):
        return self.caption
