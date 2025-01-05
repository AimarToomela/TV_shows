# Generated by Django 3.0.10 on 2025-01-05 08:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0002_auto_20250105_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='favorite_user',
            field=models.ManyToManyField(blank=True, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
