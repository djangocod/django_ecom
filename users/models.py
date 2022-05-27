

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.
class CustomManager(BaseUserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is satff must be True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is superuser must be True')

        if extra_fields.get('is_active') is not True:
            raise ValueError('is active must be True')

        user = self.create_user(username, email, password, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, email, password, **extra_fields):
        email = self.normalize_email(email)
        if not email:
            raise ValueError('email is required')
        user = self.model(username=username, email=email,
                          password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=200, unique=True,
                                help_text='username must be unique', blank=False, null=False)
    email = models.CharField(max_length=200, unique=True,
                             help_text='email must be unique', blank=False, null=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.username


class TakeMessage(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)
    subject = models.CharField(max_length=200, null=False, blank=False)
    message_body = models.TextField(null=False, blank=False)
    send_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} == {self.send_at}'
