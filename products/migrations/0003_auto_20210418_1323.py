# Generated by Django 3.1.7 on 2021-04-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_info'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]