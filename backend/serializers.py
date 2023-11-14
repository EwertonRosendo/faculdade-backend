from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Password, Users


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password']
    
    def validate_user(self, username, email):
        if Users.objects.filter(username=username) or Users.objects.filter(email=email):
            print('usuario já existe')
            return False
        print('usuario pode ser criado')
        return True
    
class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Password
        fields = ['lenghtPassword','password', 'user_id']