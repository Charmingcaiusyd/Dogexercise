# Generated by Django 4.0.3 on 2023-08-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0027_remove_community_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='title'),
        ),
    ]