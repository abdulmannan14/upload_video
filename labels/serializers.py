

from rest_framework import serializers
from django.contrib.auth.models import User

from labels.models import Label
from video.models import User_Label


class Lebel_serializer(serializers.ModelSerializer):
    class Meta:
        model=Label
        fields="__all__"


class Reaction_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Label
        fields="__all__"