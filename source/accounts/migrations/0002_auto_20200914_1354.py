# Generated by Django 2.2 on 2020-09-14 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': {('can_view_user_list', 'Can view the list of users')}, 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
