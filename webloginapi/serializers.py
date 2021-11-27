from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id','password','email',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        user = User(
            username=self.validated_data['email'],
            email=self.validated_data['email']
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user