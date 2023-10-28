from django.urls import path
from .views import UserView, PasswordView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('password/',PasswordView.as_view() )
    #path('stores/', StoresView.as_view())
    
]