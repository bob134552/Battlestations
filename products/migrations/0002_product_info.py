# Generated by Django 3.1.7 on 2021-04-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='info',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]
