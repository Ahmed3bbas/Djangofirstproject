# Generated by Django 3.1.2 on 2020-11-01 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userapp', '0003_auto_20201101_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='portfolio_site',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
