# Generated by Django 3.2.13 on 2022-07-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20220722_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforservice',
            name='requested_by',
            field=models.CharField(default='-', max_length=100),
            preserve_default=False,
        ),
    ]
