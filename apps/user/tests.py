from django.test import TestCase
from .models import User


class UserTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(
            username="テストマン",
            email="test@email.com",
            password="123"
        )

    def test_filter(self):
        User.objects.create_user(
            username="テストマン1",
            email="test1@email.com",
            password="123"
        )
        email = "test1@email.com"
        users = User.objects.filter(email=email)
        self.assertEqual(users.count(), 1, f"{email}含む記録は一つしかないはずです。")
