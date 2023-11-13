from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def validate_user(self, username, email):
        if User.objects.filter(username=username) or User.objects.filter(email=email):
            print('usuario já existe')
            return False
        print('usuario pode ser criado')
        return True
    
class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Password
        fields = ['lengthPassword','password', 'user_id']