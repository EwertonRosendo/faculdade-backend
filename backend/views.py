from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer, PasswordSerializer
from django.core import serializers

from .models import Password
from django.contrib.auth.models import User

from password_generator import PasswordGenerator

""".@method_decorator(name="get", decorator=swagger_auto_schema(
    manual_parameters=[
        'post_slug', openapi.IN_QUERY,
        description=("A unique string value identifying requested post")
        type=openapi.TYPE_STRING,
        enum=[ps.value for ps in PostStatus],
        required=True
    ]    
)),"""


class UserView(APIView):
    #select * from users
    def get(self, request, *args, **kwargs):

        users = User.objects.all()
        data = {'users':[
            
        ]}
        for user in users:
            data['users'].append({'email':user.email, 'username':user.username, 'password':user.password})

        return Response(data)
    
    #insert into users (username, email, password) values (?, ?, ?)
    def post(self, request, *args, **kwargs):
        
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid() and serializer.validate_user(request.data['username'], request.data['email']):
            serializer.save()
            return Response({'status':'conta criada'})
        
        return Response({'error':'email  ou username já cadastrados anteriormente'})
    
class PasswordView(APIView):
    #select user_id, password from passwords
    def get(self, request, *args, **kwargs):
        passwords = Password.objects.all()
        data = {'passwords':[
            
        ]}
        for password in passwords:
            data['passwords'].append({'user_id':password.user_id, 'password':password.password})

        return Response(data)
    #insert into passwords (user_id, lenghtPassword, password) values (?, ?, ?)
    def post(self, request, *ars, **kwargs):
        
        lenPassword, user_id = request.data['lenghtPassword'], request.data['user_id']
        
        PG = PasswordGenerator()
        PG.minlen = lenPassword
        PG.maxlen = lenPassword
        password = PG.generate()
        
        serializer = PasswordSerializer(data={'lenghtPassword':lenPassword, 'password':password, 'user_id':user_id})

        
        if serializer.is_valid():
            data = {'password':password, 'status':'deu bom'}
            serializer.save()
            return Response(data)

       
        return Response({'status':'senha não armazenada'})