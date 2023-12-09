from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from RealEstate.api_response_message import *

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(
            email=email,
            password=password,
            is_super_admin=True,
            is_active=True,
            **kwargs
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_super_admin = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        "self",  # Use "self" to create a recursive relationship
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_by_user",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def has_perm(self, perm, obj=None):
        return self.is_super_admin

    def has_module_perms(self, app_label):
        return self.is_super_admin

    def __str__(self):
        return self.user_name or self.email


class Logs(models.Model):
    logid = models.BigAutoField(primary_key=True, editable=False)
    transaction_name = models.CharField(max_length=500)
    mode = models.CharField(max_length=100)
    log_message = models.TextField()
    userid = models.ForeignKey(
        "User",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="log_user_id",
    )
    ip_address = models.CharField(max_length=100, null=True, blank=True)
    system_name = models.CharField(max_length=100, null=True, blank=True)
    log_date = models.DateTimeField(auto_now=True)



class Property(models.Model):
    propertyid = models.BigAutoField(primary_key=True,editable=False)
    name = models.CharField(max_length=200)
    address = models.TextField()
    location = models.CharField(max_length=200)
    features = models.TextField()
    created_by = models.ForeignKey(
        "User",  # Use "self" to create a recursive relationship
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="properity_userid",
    )
    created_at = models.DateTimeField(auto_now_add=True)

class Units(models.Model):
    unitid = models.BigAutoField(primary_key=True,editable=False)
    property = models.ForeignKey('Property',on_delete=models.RESTRICT)
    rent_cost = models.DecimalField(max_digits=10,decimal_places=2)
    type_choices = [
        ('1BHK','1BHK'),
        ('2BHK','2BHK'),
        ('1BHK','3BHK'),
        ('4BHK','4BHK'),

    ]
    unit_type = models.CharField(max_length=5,choices=type_choices)
    created_by = models.ForeignKey(
        "User",  # Use "self" to create a recursive relationship
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="units_userid",
    )
    created_at = models.DateTimeField(auto_now_add=True)

class Tenant(models.Model):
    tenantid = models.BigAutoField(primary_key=True,editable=False)
    name = models.CharField(max_length=100)
    address = models.TextField()
    documents = models.FileField(upload_to="tenant/document",null=True,blank=True)
    unit = models.ForeignKey('Units',on_delete=models.RESTRICT)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.DateField()

