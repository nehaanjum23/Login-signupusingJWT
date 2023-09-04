from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.
#The BaseUserManager is a class provided by Django that contains a set of methods for creating and managing user accounts.
class MyUserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2 = None):
       
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email = self.normalize_email(email),
            name = name,
            tc = tc,
        )

        user.set_password(password) #set_password method, which typically handles password hashing for security.
        user.save(using=self._db)#Then, the user object is saved to the database using user.save(), specifying the database to use with using=self._db
        return user

    def create_superuser(self, email, name, tc, password=None):
        user = self.create_user(
            email,
            password=password,
            name = name,
            tc = tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


#The AbstractBaseUser is a base class provided by Django for building custom user models.
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email" #This line specifies that the email field should be used as the username field for authentication. In other words, users will log in using their email addresses.
    REQUIRED_FIELDS = ["name", "tc"] #The REQUIRED_FIELDS attribute specifies which fields, in addition to the USERNAME_FIELD, are required when creating a user.

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
#This is a property method that returns True if the user is an admin (is_admin is True), which indicates that the user is part of the staff and has access to the admin interface.
    @property
    def is_staff(self):
        return self.is_admin
