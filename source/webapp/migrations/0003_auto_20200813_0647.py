# Generated by Django 2.2 on 2020-08-13 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200807_0847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='type',
            new_name='type_old',
        ),
    ]
