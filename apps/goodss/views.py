from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import Goods, Tag, Category
from .serializers import GoodsSerializer, CategorySerializer, TagSerializer
from apps.user.authorizations import JWTAuthentication


class GoodsViewSet(viewsets.ModelViewSet):
    """
    貸出品のCRUD
    """
    queryset = Goods.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = GoodsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    カテゴリーのCRUD
    """
    queryset = Category.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    タグのCRUD
    """
    queryset = Tag.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = TagSerializer


