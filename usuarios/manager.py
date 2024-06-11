from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, 
                     username, first_name, password, **extra_fields):
        now = timezone.now()

        if not email:
            raise ValueError(_("El email es requerido"))
        
        if not first_name:
            raise ValueError(_("El nombre es requerido"))
        
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            username = username,
            first_name = first_name,
            last_login = now,
            **extra_fields
            )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, first_name, password, **otros_campos):
        return self._create_user(email, username, first_name, password, **otros_campos)
    
    def create_superuser(self, email, username, first_name, password, **otros_campos):
        otros_campos.setdefault('is_staff', True)
        otros_campos.setdefault('is_superuser', True)
        otros_campos.setdefault('is_active', True)

        if otros_campos.get("is_staff") is not True:
            raise ValueError(_("is_staff debe ser True para ser super usuario"))
        
        if otros_campos.get('is_superuser') is not True:
            raise ValueError(_("is_superuser debe ser True para ser super usuario"))
        
        return self._create_user(email, username, first_name, password, **otros_campos)
    
