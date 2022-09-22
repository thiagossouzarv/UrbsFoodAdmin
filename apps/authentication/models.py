# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
import uuid

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class EmailUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        email = kwargs["email"]
        email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not email:
            raise ValueError(_('Users must have an email address'))


        
        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
###############################################################################

class Usuario(AbstractBaseUser, PermissionsMixin):
    
    uid                         = models.UUIDField(verbose_name='Identificador Unico', default=uuid.uuid4, editable=False)
    nome                        = models.CharField('Nome', max_length=100)
    email                       = models.EmailField('Email', unique=True, null=True)
    password                    = models.CharField("Senha", max_length=100, db_column='senha')
    is_superuser                = models.BooleanField(('Administrador'), default=False, db_column='is_admin', help_text=('E administrador do sistema!'),)
    alterar_senha_proximo_login = models.BooleanField(('Alterar senha proximo login'), default=True, help_text=('Precisa alterar a senha no proximo login'),)
    is_staff                    = models.BooleanField(default=False)
    reset_senha                 = models.CharField(("Cod reset Senha"), max_length=36, null=True)

    objects = EmailUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    PASSWORD_FIELD = 'senha'
    REQUIRED_FIELDS = []

    def __str__(self):
       return self.nome
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome
###############################################################################