from django.db import models

# Create your models here.

class Password(models.Model):
    
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50)
    lenghtPassword = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str(self.user_id)
    
class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username