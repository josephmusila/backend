# Generated by Django 3.2.13 on 2022-06-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_usernotifications_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.CharField(default='-', max_length=20, verbose_name='accout-type'),
            preserve_default=False,
        ),
    ]