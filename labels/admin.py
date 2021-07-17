from django.contrib import admin
from .models import Label,User_Label
from .models import Label_types

class Labels_details(admin.ModelAdmin):
    list_display = ('id','name','type')


admin.site.register(Label,Labels_details)


class User_video_display(admin.ModelAdmin):
    list_display = ('id','user','video','type','lebels')

admin.site.register(User_Label,User_video_display)
admin.site.register(Label_types)