# Generated by Django 3.2.13 on 2022-07-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_alter_requestforservice_requested_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestforservice',
            name='test',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]