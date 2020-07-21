from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from .authorizations import generate_jwt, JWTAuthentication
from .serializers import UserSerializer
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
        user = UserSerializer(source=request.data)
        if user.validated_data():
            pass

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

