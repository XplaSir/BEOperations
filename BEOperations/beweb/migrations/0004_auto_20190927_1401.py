# Generated by Django 2.2.3 on 2019-09-27 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beweb', '0003_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
