__author__ = "ハリネズミ"
from rest_framework import serializers
from .models import Goods, Category, Tag
from apps.user.serializers import UserSerializer


class GoodsSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        help_text="ログインしてるユーザー"
    )

    class Meta:
        model = Goods
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        help_text="ログインしてるユーザー"
    )

    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        help_text="ログインしてるユーザー"
    )

    class Meta:
        model = Tag
        fields = "__all__"
