# Generated by Django 3.2.13 on 2022-07-09 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_requestforservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforservice',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
