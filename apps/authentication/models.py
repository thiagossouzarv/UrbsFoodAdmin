# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,UserManager

class User(AbstractBaseUser,PermissionsMixin):

    username = models.CharField('Nome de Usuário',max_length=30,unique=True)
    email = models.EmailField('E-mail',unique=True)
    name = models.CharField('Nome',max_length=100,blank=True)
    is_active = models.BooleanField('Está Ativo?',blank=True,default=True)
    is_staff = models.BooleanField('Administrador?',blank=True,default=False)
    date_joined = models.DateTimeField('Data de Entrada',auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
