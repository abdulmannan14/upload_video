from django.shortcuts import render
from .models import Video
from django.http import JsonResponse
from rest_framework.views import APIView
# @login_required(login_url='/login')
from .serializers import Video_Serializer


class Video_page(APIView):
    def get (self,request):
        listi=[]
        username = request.user.username
        video = Video.objects.all()
        for i in video:
            users_to_show_whom=i.show_to
            if username in users_to_show_whom:
                vedio_serializer = Video_Serializer(i, many=False).data
                listi.append(vedio_serializer)
            else:
                pass
        # lebels= Label.objects.all()
        return JsonResponse(listi, safe=False)



