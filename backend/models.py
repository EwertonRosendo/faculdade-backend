from django.db import models

# Create your models here.

class Password(models.Model):
    password = models.CharField(max_length=50)
    lengthPassword = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str(self.user_id)