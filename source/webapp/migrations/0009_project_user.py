# Generated by Django 2.2 on 2020-09-10 08:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0008_auto_20200824_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(default=1, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
