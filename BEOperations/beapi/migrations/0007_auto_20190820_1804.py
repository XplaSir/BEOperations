# Generated by Django 2.2.3 on 2019-08-20 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beapi', '0006_auto_20190819_1114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='teamleader',
            options={'managed': False},
        ),
    ]
