# Generated by Django 4.0.3 on 2023-08-21 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_seller_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Goods',
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': 'goods', 'verbose_name_plural': 'goods'},
        ),
        migrations.AlterModelTable(
            name='goods',
            table='goods',
        ),
    ]
