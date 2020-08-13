# Generated by Django 2.2 on 2020-08-13 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200813_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ManyToManyField(related_name='task_type', to='webapp.Type', verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type_old',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task_type_old', to='webapp.Type', verbose_name='Тип'),
        ),
    ]
