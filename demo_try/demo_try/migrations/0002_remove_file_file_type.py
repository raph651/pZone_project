# Generated by Django 4.0 on 2022-08-17 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo_try', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file_type',
        ),
    ]
