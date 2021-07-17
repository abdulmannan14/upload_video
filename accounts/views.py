from django.contrib.auth import login
from django.http import JsonResponse
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer,register_serializer,ChangePasswordSerializer
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        print("entered")
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print("second")
        login(request, user)
        print(LoginAPI)
        print("last")
        return super(LoginAPI, self).post(request,format=None)

class Register(APIView):
    def post(self,request):
        serializer = register_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            if User.objects.filter(username=username).first():
                return JsonResponse("this username has been already taken",safe=False)
            if User.objects.filter(email=email).first():
                return JsonResponse("this emails has been already taken",safe=False)
            user_obj = User(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            return JsonResponse("successfully created user",safe=False)
        except Exception as e:
            print(e)
            return JsonResponse("please enter data to get registered",safe=False)




class Change_Pass(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class Get_user_data(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user_id=request.user.id
        get_user = User.objects.get(id=user_id)
        user_serializer = UserSerializer(get_user,many=False).data
        return JsonResponse(user_serializer,safe=False)