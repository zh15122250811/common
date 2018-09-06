from django.db import models

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=256)
    gender = models.BooleanField(default=True)
    email = models.CharField(max_length=100,unique=True)
    icon = models.ImageField(upload_to="icons")
    isdelete = models.BooleanField(default=False)

    class Meta:
        db_table = "userinfo"