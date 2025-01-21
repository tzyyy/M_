#!/usr/bin/python
# -*- coding: UTF-8 -*-
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User as CustomUser
from .serializers import UserSerializer
from .utils import login_utils


class SignUpView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = login_utils.generate_user_password(request.data.get('password'))

        if CustomUser.objects.filter(email=email).exists():
            return Response({"error": "User already exists!"},
                            status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create(email=email, password=password)

        return Response({"id": user.id, "email": email}, status=status.HTTP_400_BAD_REQUEST)


class SignInView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = CustomUser.objects.filter(email=email).first()
        if user:
            db_user_id = user.id
            db_password = user.password
            # 密码错误
            if not login_utils.verify_user_password(password, db_password):
                return Response({"error": "email or password error!"},
                                status=status.HTTP_400_BAD_REQUEST)
            # 响应用户信息， token
            refresh = RefreshToken.for_user(user)
            return Response({
                'id': db_user_id,
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

