from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Anecdote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        write_only_fields = 'password'

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class AnecdoteSerializer(serializers.ModelSerializer):
    author = UserInfoSerializer(read_only=True)

    class Meta:
        model = Anecdote
        fields = ['id', 'author', 'date', 'text', 'likes', 'whoLikedIt']
        read_only_fields = ['author']

    def create(self, validated_data):
        print(validated_data)
        data = {'date': validated_data['date'],
                'text': validated_data['text'],
                'likes': validated_data['likes'],
                'whoLikedIt': validated_data['whoLikedIt'],
                'author': validated_data['owner']}
        anecdote = Anecdote.objects.create(**data)
        return anecdote