# Generated by Django 5.0.4 on 2024-04-17 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum42', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
    ]