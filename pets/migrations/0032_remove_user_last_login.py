# Generated by Django 4.2.6 on 2023-11-02 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0031_user_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]