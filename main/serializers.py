from django.contrib.auth.models import User
from rest_framework import serializers, permissions

from main.models import *


class ProductSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.username'
    )

    class Meta:
        fields = '__all__'
        model = Products


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, required=True, write_only=True)
    password2 = serializers.CharField(min_length=4, required=True, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2')

    def validate(self, attrs):
        password2 = attrs['password2']
        print(password2)
        if not password2 == attrs['password']:
            raise serializers.ValidationError('Passwords did not match')
        return attrs

    def create(self, validated_data,):
        print('salam', validated_data)
        user = User.objects.create(username=validated_data['username'], first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        print('salam', validated_data)
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User

