# Generated by Django 2.2 on 2020-08-13 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20200813_0700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='type_old',
        ),
    ]
