# Generated by Django 4.0 on 2022-09-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_try', '0004_file_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('industry', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='user',
        ),
    ]
