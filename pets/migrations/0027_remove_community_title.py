# Generated by Django 4.0.3 on 2023-08-30 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0026_community_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='title',
        ),
    ]
