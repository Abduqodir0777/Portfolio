from django.db.models import Model, CharField, EmailField, ForeignKey, CASCADE, PositiveIntegerField, ManyToManyField
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class User(AbstractUser):
    job = CharField(max_length=150, null=True, blank=True)
    phone_number = CharField(max_length=30, unique=True, null=True, blank=True)

    groups = ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = ManyToManyField(Permission, related_name='custom_user_permissions_set', blank=True)


class Skills(Model):
    user = ForeignKey('apps.User', on_delete=CASCADE)
    title = CharField(verbose_name='skill nomi', max_length=150)
    level = PositiveIntegerField()
