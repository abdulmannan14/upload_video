from rest_framework import serializers
from django.contrib.auth.models import User

from labels.models import Label
from .models import Video
# User Serializer
class Video_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"