from django.db import models

# Create your models here.

class Password(models.Model):
    password = models.CharField(max_length=50)
    lengthPassword = models.IntegerField(default=10)
    user_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str(self.user_id)