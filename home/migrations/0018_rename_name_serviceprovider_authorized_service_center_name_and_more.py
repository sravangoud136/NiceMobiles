# Generated by Django 4.0.4 on 2022-05-08 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0017_remove_job_pop_date_job_part_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceprovider',
            old_name='name',
            new_name='authorized_service_center_name',
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='password',
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='username',
        ),
        migrations.AddField(
            model_name='job',
            name='EstimatedCost',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='email_id',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
