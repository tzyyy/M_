from django.db import models


# Create your models here.

# class CustomUser(models.Model):
#     id = models.BigAutoField(primary_key=True, verbose_name='用户')
#     email = models.CharField(verbose_name='email', unique=True, max_length=100)
#     password = models.CharField(verbose_name='登录密码', max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'login_account'
#         db_table_comment = '用户登陆表'
#         verbose_name = verbose_name_plural = '用户登陆表'


from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


#  Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


#  Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        managed = False
        db_table = 'login_account'
        db_table_comment = '用户登陆表'
        verbose_name = verbose_name_plural = '用户登陆表'

    def __str__(self):
        return self.email


"""
 python manage.py makemigrations
python manage.py migrate


"""
