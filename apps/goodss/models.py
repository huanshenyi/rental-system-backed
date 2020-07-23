from django.db import models
from django.contrib.auth import get_user_model
from apps.user.models import Group
User = get_user_model()


class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "削除"),
    )
    name = models.CharField(max_length=50, verbose_name="カテゴリー")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状態")
    is_nav = models.BooleanField(default=False, verbose_name="ナビに表示するか")
    owner = models.ForeignKey(User, verbose_name="作成者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="追加時間")

    class Meta:
        verbose_name = verbose_name_plural = "カテゴリー"


class Tag(models.Model):
    """
    部品に足せるタグ
    """
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "削除"),
    )
    name = models.CharField(max_length=20, verbose_name="タグ名")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状態")
    owner = models.ForeignKey(User, verbose_name="作成者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="追加時間")
    user_group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = verbose_name_plural = "タグ"


class Goods(models.Model):
    """
    貸出用の部品
    """
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '削除'),
        (STATUS_DRAFT, '編集中')
    )
    name = models.CharField(max_length=255, verbose_name="品名", db_index=True)
    desc = models.CharField(max_length=1024, verbose_name="紹介", blank=True)
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="ステータス")
    image = models.ImageField(max_length=200, upload_to="goods/", null=True, default="", blank=True)
    owner = models.ForeignKey(User, verbose_name="作成者", on_delete=models.CASCADE)
    user_group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name="分類")
    tag = models.ManyToManyField(Tag, verbose_name="タグ")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="追加時間")

    class Meta:
        verbose_name = verbose_name_plural = "貸出品"
        ordering = ['-id']

    def __str__(self):
        return self.name


