from rest_framework.views import APIView
from rest_framework.response import Response

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
        
        lenPassword, user_id = request.data['lengthPassword'], request.data['user_id']
        
        PG = PasswordGenerator()
        PG.minlen = lenPassword
        PG.maxlen = lenPassword
        password = PG.generate()
        
        serializer = PasswordSerializer(data={'lengthPassword':lenPassword, 'password':password, 'user_id':user_id})

        
        if serializer.is_valid():
            data = {'password':password, 'status':'deu bom'}
            serializer.save()
            return Response(data)

       
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
    def delete(self, request, *args, **kwargs):
        password_id = kwargs.get('pk')
        password = get_object_or_404(Password, id=password_id)
        password.delete()
        return Response({'status': 'Senha excluída com sucesso'})