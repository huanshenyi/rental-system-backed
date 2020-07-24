from django.shortcuts import render
from rest_framework import viewsets, views, status
from rest_framework.permissions import IsAuthenticated
from .models import Goods
from .serializers import GoodsSerializer
from apps.user.authorizations import JWTAuthentication


class GoodsViewSet(viewsets.ModelViewSet):
    """
    貸出品のCRUD
    """
    queryset = Goods.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = GoodsSerializer

