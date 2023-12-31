# Generated by Django 4.0.3 on 2023-08-28 07:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0019_alter_goods_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('desc', models.TextField(verbose_name='desc')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('category_name', models.CharField(max_length=255, verbose_name='category name')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create time')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.seller', verbose_name='seller')),
            ],
            options={
                'verbose_name': 'services',
                'verbose_name_plural': 'services',
                'db_table': 'services',
            },
        ),
    ]
