from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.user.authorizations import JWTAuthentication
from .serializers import PeriodSerializers


class PeriodViewSet(viewsets.ModelViewSet):
    """
    貸出の期間登録
    """
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = PeriodSerializers

