from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import UserSerializer, PasswordSerializer
from django.core import serializers
from drf_spectacular.utils import extend_schema
from .models import Password, Users


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

        users = Users.objects.all()
        data = {'users':[
            
        ]}
        for user in users:
            data['users'].append({'id':user.id, 'email':user.email, 'username':user.username, 'password':user.password})

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
        if request.data:
            data = request.data
        else:
            data = {
                    "email":"Luquinhas@com",
                    "username":"luquinhas123morango",
                    "password":"manobrown"
}
        user = Users.objects.get(id=data['id'])
        serializer = UserSerializer(instance=user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'deu bom'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete from users where id = ?
    @extend_schema(responses=UserSerializer)
    def delete(self, request, *args, **kwargs):
        user = Users.objects.get(id=request.data['id'])
        user.delete()
        return Response({'status':'deletado com sucesso'}, status=status.HTTP_202_ACCEPTED)
    
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
    """# select * from passwords where id = ?
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
        return Response({'status':'deletado com sucesso'}, status=status.HTTP_202_ACCEPTED)"""