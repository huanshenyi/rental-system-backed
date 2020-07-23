import os

from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from backed import settings
from .authorizations import generate_jwt, JWTAuthentication
from .serializers import UserSerializer
import shortuuid
User = get_user_model()


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            user = serializer.validated_data.get("user")
            user.last_login = now()
            user.save()
            token = generate_jwt(user)
            user_serializer = UserSerializer(user)
            return Response(data={"token": token, "user": user_serializer.data})
        else:
            print(serializer.errors)
            return Response(data={"message": "提出データエラー"})


class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # TODO:同じ所属のユーザーしか見れないのが普通
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        ser = UserSerializer(data=request.data)
        if ser.is_valid():
            try:
                User.objects.create_user(
                    username=ser.validated_data["username"],
                    password=request.data["password"],
                    user_group=request.user.user_group
                )
            except ValueError:
                return Response(data={"message": "ValueError"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"message": ser.error_messages}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

    def put(self, request):
        user = request.user
        user.username = request.data.get("username")
        user.telephone = request.data.get("telephone", None)
        user.email = request.data.get("email")
        user.avatar = request.data.get("avatar")
        user.user_group = request.data.get("user_group")
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class AvatarUploadView(APIView):
    """
    アイコンのアップロード
    """
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def save_file(self, file):
        # obj.jpg => (obj, ipg)
        filename = shortuuid.uuid() + os.path.splitext(file.name)[-1]
        with open(os.path.join(settings.MEDIA_ROOT, filename), "wb") as fp:
            for chunk in file.chunks():
                fp.write(chunk)
            return settings.MEDIA_URL + filename

    def post(self, request):
        file = request.FILES.get("file")
        filepath = self.save_file(file)
        # base urlに元ついてurlを生成する
        fileurl = request.build_absolute_uri(filepath)
        return Response({"picture": fileurl})

