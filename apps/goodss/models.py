from django.db import models


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "削除"),
    )
    name = models.CharField(max_length=20, verbose_name="タグ名")


class Goods(models.Model):
    """
    貸出用の商品
    """
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '削除'),
        (STATUS_DRAFT, '編集中')
    )
    name = models.CharField(max_length=255, verbose_name="部品名")
    desc = models.CharField(max_length=1024, verbose_name="紹介", blank=True)
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="ステータス")

