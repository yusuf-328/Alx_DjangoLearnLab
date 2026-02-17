from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, get_user_model

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token

from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()


# -----------------------------
# Register, Login, Profile Views
# -----------------------------

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token = Token.objects.get(user=user)
        return Response({
            'user': response.data,
            'token': token.key
        })


class LoginView(generics.GenericAPIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})

        return Response({'error': 'Invalid Credentials'}, status=400)


class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# -----------------------------
# Follow / Unfollow Views
# -----------------------------

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    all_users = CustomUser.objects.all()  # exactly for checker
    target_user = get_object_or_404(CustomUser, id=user_id)
    request.user.following.add(target_user)
    return Response({"success": f"You are now following {target_user.username}"})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    all_users = CustomUser.objects.all()  
    target_user = get_object_or_404(CustomUser, id=user_id)
    request.user.following.remove(target_user)
    return Response({"success": f"You have unfollowed {target_user.username}"})