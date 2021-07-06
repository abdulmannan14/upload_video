from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from labels.views import *
from video.views import *
from accounts.views import *
from knox import views as knox_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/video/', Video_page.as_view(), name='video'),
    path('api/lebels/', Labels.as_view(), name='lebles'),
    path('api/reactions/', User_reactions.as_view(), name='User_reaction'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
