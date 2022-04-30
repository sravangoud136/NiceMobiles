# Generated by Django 4.0.4 on 2022-04-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_job_jobstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jobStatus',
            field=models.CharField(choices=[('REGISTERED', 'Registered'), ('IN_PROGRESS', 'In Progress'), ('CLOSED', 'Closed'), ('DELIVERED', 'Delivered')], default='REGISTERED', max_length=20),
        ),
    ]
