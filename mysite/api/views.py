from .serializers import UserDetailSerializer, UserPersonalSerializer, ExtraInfoSerializer,LoginSerializer
from rest_framework import viewsets,permissions
from user.models import UserDetail, UserPersonal, ExtraInfo
from rest_framework.views import APIView
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class UserDetailView(viewsets.ModelViewSet):
    throttle_scope = 'userdetail'
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserPersonalView(viewsets.ModelViewSet):
    throttle_scope = 'userpersonal'
    queryset = UserPersonal.objects.all()
    serializer_class = UserPersonalSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ExtraInfoView(viewsets.ReadOnlyModelViewSet):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LoginView(APIView):
    def post(self,request, *args, **kwargs):
        serializer= LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key},status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self,request):
        django_logout(request)
        return Response(status=204)

