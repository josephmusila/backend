# Generated by Django 3.2.13 on 2022-08-27 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_alter_requestforservice_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestforservice',
            name='test',
        ),
    ]
