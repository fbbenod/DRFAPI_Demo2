from rest_framework import serializers
from user.models import UserDetail, UserPersonal, ExtraInfo
from django.contrib.auth import authenticate,login
from rest_framework import exceptions
from django.contrib.auth.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserDetail
        fields= ('Name','Address','Phone')


class UserPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPersonal
        fields= ('Blog',)


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields=('FatherName','Citizenship')


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):
        username=data.get("username", " ")
        password=data.get("password", " ")

        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data["user"]=user
                else:
                    msg = "User is deactivated"
                    raise exceptions.ValidationError(msg)
            else:
                msg= "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = " Must provide username and password both "
            raise exceptions.ValidationError(msg)
        return data






