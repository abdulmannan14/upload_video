from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
# @login_required(login_url='/login')
from video.models import User_Label
from .models import Label
from .serializers import Lebel_serializer


class Labels(APIView):
    def get(self,request):
        lebel= Label.objects.all()
        print("thes are labels",lebel)
        lebel_serializer = Lebel_serializer(lebel,many=True).data
        return JsonResponse(lebel_serializer,safe=False)


class User_reactions(APIView):

    def delete(self,request):
        data = request.data
        user_id = data.get('user_id')
        video_id = data.get('video_id')
        lebel_id = data.get('lebel_id')
        try:
            reaction=User_Label.objects.get(user_id=user_id,video_id=video_id,lebels_id=lebel_id)
            reaction.delete()
            return JsonResponse("deleted", safe=False)
        except:
            return JsonResponse("No data found", safe=False)

    def post(self,request):
        data= request.data
        user_id=data.get('user_id')
        video_id=data.get('video_id')
        lebel_id=data.get('lebel_id')
        user_model= User_Label(user_id=user_id,video_id=video_id,lebels_id=lebel_id)
        try:
            User_Label.objects.get(user_id=user_id,video_id=video_id,lebels_id=lebel_id)
            return JsonResponse("data already exists", safe=False)
        except:
            user_model.save()
            return JsonResponse("data saved", safe=False)

