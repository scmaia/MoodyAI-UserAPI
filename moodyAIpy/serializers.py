from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import AIResponse

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email')
        write_only_fields = ('password',)
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class AIResponseSerializer(serializers.ModelSerializer):
  class Meta:
    model = AIResponse 
    fields = ('pk', 'user', 'prompt', 'response', 'mood', 'favorite', 'created_at')