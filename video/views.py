from django.shortcuts import render
from .models import User_Videos
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

@login_required(login_url='/login')
def index(request):
    listi=[]
    username = request.user.username
    print("%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& this is the requested user  %%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",username)
    video = User_Videos.objects.all()
    for i in video:
        users_to_show_whom=i.show_to
        if username in users_to_show_whom:
            listi.append(i)
        else:
            pass

    return render(request, 'index.html', {"video": listi})


