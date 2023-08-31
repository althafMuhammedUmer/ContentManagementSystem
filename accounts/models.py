from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import EmailValidator, MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, phone, pincode, password=None):
        if not email:
            raise ValueError("User must have an email address")
        
        user = self.model(
            email = (self.normalize_email(email)).lower(),
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            pincode = pincode
        )

        user.set_password(password)
        user.save(using=self._db)
        

        return user
    
    def create_superuser(self, email, first_name, last_name, phone, pincode, password=None):
        user = self.create_user(
            email = email,
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            password=password,
            pincode=pincode

        )

        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)

        return user





class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, validators=[EmailValidator(message="Invalid email format")])
    password = models.CharField(max_length=200, validators=[MinLengthValidator(8, message="Password must be minimum 8 length"), RegexValidator(r'[A-Z]', message="must contain at least 1 uppercase character"), RegexValidator(r'[a-z]', message="must contiane at least 1 lowercase character")])
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message="phone number must be 10 digits")])
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=6 , validators=[RegexValidator(r'^\d{6}$', message="Pincode must be 6 digits")])

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'pincode']


    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def get_all_permissions(user=None):
        if user.is_superuser:
            return set()
    
    


    





