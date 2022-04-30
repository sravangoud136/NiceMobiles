# Generated by Django 4.0.4 on 2022-04-16 13:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_job_id_alter_job_customername_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='jobReferenceNumber',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
