# Generated by Django 3.2.13 on 2022-07-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_requestforservice_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforservice',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]
