# Generated by Django 4.0.3 on 2023-08-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='temperament',
            field=models.CharField(default='', max_length=255, verbose_name='temperament'),
        ),
    ]