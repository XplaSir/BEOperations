# Generated by Django 2.2.3 on 2019-08-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('centre_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('centre_code', models.CharField(blank=True, max_length=100, null=True)),
                ('centre_name', models.CharField(blank=True, max_length=100, null=True)),
                ('cost_centre', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'centre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JobStatus',
            fields=[
                ('job_status_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'job_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('job_type_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'job_type',
                'managed': False,
            },
        ),
    ]
