from django.db.models import Model, CharField, EmailField, ForeignKey, CASCADE, PositiveIntegerField, ManyToManyField
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class User(AbstractUser):
    first_name = CharField(verbose_name='ism', max_length=222, null=True, blank=True)
    last_name = CharField(verbose_name='familya', max_length=200)
    username = CharField(max_length=200, unique=True)
    job = CharField(verbose_name='kasbi', max_length=150)
    phone_number = CharField(verbose_name='telefon raqami', max_length=30, unique=True)
    email = EmailField(verbose_name='pochta manzil', max_length=150, unique=True)

    
    groups = ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = ManyToManyField(Permission, related_name='custom_user_set', blank=True)
    

class Skills(Model):
    user = ForeignKey('apps.User', on_delete=CASCADE)
    title = CharField(verbose_name='skill nomi', max_length=150)
    level = PositiveIntegerField()
    