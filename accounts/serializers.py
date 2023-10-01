from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']
        extra_kwargs = {
            'phone_number': {'required': True}, 'email': {'required': True},
        }


class EditUserSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'first_name', 'last_name', 'biography', 'photo']

    def get_photo(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url)
        else:
            return None
