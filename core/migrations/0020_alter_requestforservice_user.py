# Generated by Django 3.2.13 on 2022-07-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_requestforservice_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforservice',
            name='user',
            field=models.TextField(max_length=50),
        ),
    ]
