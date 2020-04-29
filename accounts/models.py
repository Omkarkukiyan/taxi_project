from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address") 
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
             email=self.normalize_email(email),
             username = username,
        ) 
        user.set_password(password)
        user.save(using=self._db)
        return user   


    def create_user_for_rider(self, email, username,first_name, last_name,profile_pic,is_rider, password1=None):
        if not email:
            raise ValueError("Users must have an email address") 
        if not username:
            raise ValueError("Users must have an username")
        if not first_name:
            raise ValueError("Users must have an firstname")
        if not last_name:
            raise ValueError("Users must have an lastname")        
        
        user = self.model(
             email=self.normalize_email(email),
             username = username,
             first_name = first_name,
             last_name = last_name,
             is_rider=is_rider,
             profile_pic=profile_pic
        ) 
        user.set_password(password1)
        user.save(using=self._db)
        return user   


    def create_user_for_driver(self, email, username,first_name, last_name,is_driver, license_id,profile_pic,password1=None):
        if not email:
            raise ValueError("Users must have an email address") 
        if not username:
            raise ValueError("Users must have an username")
        if not first_name:
            raise ValueError("Users must have an firstname")
        if not last_name:
            raise ValueError("Users must have an lastname")   
        if not license_id:
            raise ValueError("Üser must have a license number")         
        
        user = self.model(
             email=self.normalize_email(email),
             username = username,
             first_name = first_name,
             last_name = last_name,
             is_driver=is_driver,
             license_id = license_id,
             profile_pic=profile_pic
        ) 
        user.set_password(password1)
        user.save(using=self._db)
        return user     
      

    def create_superuser(self, email, username,password, **kwargs): 
        user = self.create_user(
               email = self.normalize_email(email),
               username = username,
               password=password,
               **kwargs    
            ) 
        user.is_rider = False
        user.is_driver = False   
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    
    first_name  = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(verbose_name='email', max_length=60, unique = True)
    profile_pic = models.ImageField(upload_to='photos/%Y/%m/%d/',default='default.jpg')
    license_id = models.CharField(max_length=10, validators=[alphanumeric], blank=True) 
    is_driver = models.BooleanField(default=False)
    is_rider = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None): 
        return self.is_admin

    def has_module_perms(self,app_label):
        return True    
