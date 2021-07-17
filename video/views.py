import django.conf
import django_base_url
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from .models import Video
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import Video_Serializer


# class Video_page(APIView):
#     def get (self,request):
#         listi=[]
#         username = request.user.username
#         id = request.user.id
#         video = Video.objects.all()
#         for i in video:
#             users_to_show_whom=i.show_to.id
#             print("this is to show whom:",users_to_show_whom)
#             if id == users_to_show_whom:
#                 print("entered in if")
#                 vedio_serializer = Video_Serializer(i, many=False).data
#                 listi.append(vedio_serializer)
#             else:
#                 pass
#         # lebels= Label.objects.all()
#         return JsonResponse(listi, safe=False)

class Video_page(APIView):
    permission_classes = (IsAuthenticated,)
    def get (self,request):
        username = request.user.username
        video = Video.objects.filter(show_to__username=username)
        vedio_serializer = Video_Serializer(video, many=True).data
        return JsonResponse(vedio_serializer, safe=False)

