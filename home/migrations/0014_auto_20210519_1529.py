# Generated by Django 3.1.7 on 2021-05-19 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20210514_1905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitereviews',
            options={'ordering': ('-date',), 'verbose_name_plural': 'Site Reviews'},
        ),
    ]