# Generated by Django 2.2 on 2020-09-10 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_project_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('add_remove_user', 'добавление и удаление юзера')], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
    ]