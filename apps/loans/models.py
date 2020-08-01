from django.db import models
from django.contrib.auth import get_user_model
from apps.goodss.models import Goods
User = get_user_model()


class Period(models.Model):
    """
    貸出の期間登録
    """
    STATUS_CHECKIN = 1
    STATUS_COMPLETE = 2
    STATUS_NOTHING = 0
    STATUS_ITEMS = (
        (STATUS_CHECKIN, "チェックイン"),
        (STATUS_NOTHING, "未チェックイン"),
        (STATUS_COMPLETE, "返却完了")
    )

    owner = models.ForeignKey(User, verbose_name="ユーザー", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="貸出品", on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=1, verbose_name="貸出数")
    status = models.PositiveIntegerField(default=STATUS_NOTHING, choices=STATUS_ITEMS, verbose_name="状態")
    comment = models.CharField(null=True, max_length=1024, verbose_name="コメント", blank=True)
    plans_return_time = models.DateTimeField(verbose_name="予定返却時間")
    returned_time = models.DateTimeField(null=True, verbose_name="実際返却時間")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="追加時間")

    class Meta:
        verbose_name = "貸出スケジュール"
        verbose_name_plural = verbose_name
        unique_together = ("owner", "goods")

    def __str__(self):
        return "-%s(%d)".format(self.goods.name, self.goods_num)


