# Generated by Django 3.2.13 on 2022-07-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_rename_date_created_requestforservice_job_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestforservice',
            name='date_requested',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='requestforservice',
            name='job_date',
            field=models.DateField(),
        ),
    ]
