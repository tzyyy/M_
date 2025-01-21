#!/usr/bin/python
# -*- coding: UTF-8 -*-
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class UserCenterViewSet(GenericViewSet, mixins.RetrieveModelMixin):
    # 也可局部配置认证
    authentication_classes = [JSONWebTokenAuthentication]
    # 设置必须登录才能访问的权限类
    permission_classes = [IsAuthenticated, ]

    queryset = models.User.objects.filter(is_active=True).all()
    serializer_class = serializers.UserCenterSerializer