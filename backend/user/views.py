from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserRegister(CreateAPIView):
    serializer_class = UserRegisterSerializer

class UserLogin(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
 
        user = authenticate(username=username,password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response({"error": "Invalid credentials"}, status=400)

class UserLogout(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            # Delete the user's token
            Token.objects.get(user=request.user).delete()
        except Token.DoesNotExist:
            pass  # Token not found

        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)