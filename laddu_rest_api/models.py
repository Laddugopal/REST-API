from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
#User profile manager
from django.contrib.auth.models import BaseUserManager
# user profile manager class


class UserProfileManager(BaseUserManager):
    '''
        Manager for user profiles
    '''    
    def create_user(self,email,name,password=None):
        '''
            Create a new user profile
        '''
        if not email:
            raise ValueError("Must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def super_user(self, email, name, password):
        ''' 
            Create a user and save it as a super user
        
        '''
        
        user = self.create_user(self, email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)
        
        return user


    
class UserProfile(AbstractBaseUser,PermissionsMixin): 
    '''
        Database model for users in the system
    '''
    email = models.EmailField(max_length = 255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        '''
            retrieves the full name of the user
        '''
        return self.name
    
    def get_short_name(self):
        '''
            Retrieves the short name of the user
        '''
        return self.name
    
    def __str__(self):
        '''Return string representation of the user'''
        return self.email
    