from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from api.models import User 


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            User = serializer.save()
        return Response({'msg' : 'Registration Successfull'})


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception = True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email = email, password = password)
            if user is not None:
                return Response({'msg' : 'Login Sucessfull'},status=status.HTTP_200_OK)
            else:
                return Response({'msg' : 'error'},status=status.HTTP_400_BAD_REQUEST)

