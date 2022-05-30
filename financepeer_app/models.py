from django.db import models
from postgres_copy import CopyManager

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="User ID")
    name = models.CharField(max_length=500, verbose_name="User name", unique=True)
    username = models.CharField(max_length=500, verbose_name="username", unique=True)
    password = models.CharField(max_length=500,verbose_name="password")
    login_flag = models.BooleanField(verbose_name="created time", default=False)

    objects_copy_manager = CopyManager()
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'users'

class Usersdata(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="User ID")
    userid = models.IntegerField(verbose_name="User name")
    title = models.CharField(max_length=5000, verbose_name="title")
    body = models.CharField(max_length=9000, verbose_name="body")

    objects_copy_manager = CopyManager()
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'usersdata'