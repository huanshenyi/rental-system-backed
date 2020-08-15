"""
user.User  ModelのCRUD
user.Group ModelのCRUD
"""
from django.test import TestCase
from .models import User, Group


class UserTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(
            username="テストマン",
            email="test@email.com",
            password="123"
        )

    def test_create(self):
        user = User.objects.create_user(
            username="テストマン1",
            email="test1@email.com",
            password="123"
        )
        self.assertEqual(user.username, "テストマン1", "ユーザーネームが一致しません。")

    def test_filter(self):
        User.objects.create_user(
            username="テストマン2",
            email="test1@email.com",
            password="123"
        )
        email = "test1@email.com"
        users = User.objects.filter(email=email)
        self.assertEqual(users.count(), 1, f"{email}含む記録は一つしかないはずです。")

    def test_changeStatus(self):
        user = User.objects.filter(username="テストマン1")
        user.is_active = False
        self.assertEqual(user.is_active, False, "ステータス修正されました。")

    def test_DeleteUser(self):
        User.objects.filter(username="テストマン1").delete()
        user = User.objects.filter(username="テストマン1")
        self.assertEqual(user.count(), 0, "削除行われませんでした。")


class GroupTestCase(TestCase):
    def setUp(self) -> None:
        Group.objects.create(
            name="テストグループ",
            owner=1
        )

    def test_group_create(self):
        group = Group.objects.first()
        self.assertEqual(group.name, "テストグループ", "グループの名前が一致しません。")

    def test_change(self):
        group = Group.objects.first()
        group.name = "修正後名前"
        self.assertEqual(group.name, "修正後名前", "名前の修正失敗しました。")

    def test_delete(self):
        Group.objects.filter(name="テストグループ").delete()
        group = Group.objects.filter(name="テストグループ")
        self.assertEqual(group.count(), 0, "削除行われませんでした。")
