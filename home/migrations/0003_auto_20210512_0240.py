# Generated by Django 3.1.7 on 2021-05-12 02:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_sitereviews_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitereviews',
            name='rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1, editable=False),
        ),
        migrations.AlterField(
            model_name='sitereviews',
            name='review',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='sitereviews',
            name='user',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
