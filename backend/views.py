from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import UserSerializer, PasswordSerializer
from django.core import serializers
from drf_spectacular.utils import extend_schema
from .models import Password
from django.contrib.auth.models import User

from password_generator import PasswordGenerator
from django.shortcuts import get_object_or_404

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
    @extend_schema(responses=UserSerializer)
    def get(self, request, *args, **kwargs):

        users = User.objects.all()
        data = {'users':[
            
        ]}
        for user in users:
            data['users'].append({'email':user.email, 'username':user.username, 'password':user.password})

        return Response(data)
    
    #insert into users (username, email, password) values (?, ?, ?)
    @extend_schema(responses=UserSerializer)
    def post(self, request, *args, **kwargs):
        
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid() and serializer.validate_user(request.data['username'], request.data['email']):
            serializer.save()
            return Response({'status':'conta criada'})
        
        return Response({'error':'email  ou username já cadastrados anteriormente'})
    
    # select * from users where id = ?
    @extend_schema(responses=UserSerializer)
    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(instance=user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Usuário atualizado com sucesso'})
        
        return Response({'error': 'Erro na atualização do usuário'})

    # delete from users where id = ?
    @extend_schema(responses=UserSerializer)
    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response({'status': 'Usuário excluído com sucesso'})
    
class PasswordView(APIView):
    #select user_id, password from passwords
    @extend_schema(responses=PasswordSerializer)
    def get(self, request, *args, **kwargs):
        passwords = Password.objects.all()
        data = {'passwords':[
            
        ]}
        for password in passwords:
            data['passwords'].append({'user_id':password.user_id, 'password':password.password})

        return Response(data)
    #insert into passwords (user_id, lenghtPassword, password) values (?, ?, ?)
    @extend_schema(responses=PasswordSerializer)
    def post(self, request, *args, **kwargs):
        if request.data:
            data = request.data        
        
            
            
        
        PG = PasswordGenerator()
        PG.minlen = 1
        PG.maxlen = 10
        password = PG.generate()
        

        serializer = PasswordSerializer(data={'password':password,'lengthPassword':request.data['lengthPassword'], 'user_id':request.data['user_id']})
        #serializer = PasswordSerializer(data=data)
        
        if serializer.is_valid() :
            serializer.save()
            return Response({'status':'senha cadastrado'}, status=status.HTTP_201_CREATED)
       
        return Response({'status':'senha não armazenada'})
    # select * from passwords where id = ?
    @extend_schema(responses=PasswordSerializer)
    def put(self, request, *args, **kwargs):
        password_id = kwargs.get('pk')
        password = get_object_or_404(Password, id=password_id)
        serializer = PasswordSerializer(instance=password, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Senha atualizada com sucesso'})
        
        return Response({'error': 'Erro na atualização da senha'})

    # delete from passwords where id = ?
    @extend_schema(responses=PasswordSerializer)
    def delete(self, request, id, *args, **kwargs):
        data = PasswordSerializer.objects.get(id=id)
        data.delete()
        return Response({'status':'deletado com sucesso'}, status=status.HTTP_202_ACCEPTED)