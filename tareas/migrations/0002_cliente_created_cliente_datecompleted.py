# Generated by Django 4.2.1 on 2023-05-15 02:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='datecompleted',
            field=models.DateTimeField(null=True),
        ),
    ]
