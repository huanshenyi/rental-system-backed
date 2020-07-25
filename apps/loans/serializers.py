__author__ = "ハリネズミ"
from rest_framework import serializers
from .models import Period
from apps.goodss.models import Goods


class PeriodSerializers(serializers.ModelSerializer):
    """
    貸出の期間登録
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        help_text='ログインしてるユーザー'
    )
    goods_num = serializers.IntegerField(required=True, min_value=1,
                                         error_messages={"min_value": "品の数は1以下あってはならない",
                                                         "required": "数を入れてください"
                                                         })
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())

    class Meta:
        model = Period
        fields = "__all__"
