# Generated by Django 5.0.6 on 2024-07-07 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_user_password1_user_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
    ]