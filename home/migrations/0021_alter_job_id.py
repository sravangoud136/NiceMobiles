# Generated by Django 4.0.4 on 2022-06-25 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_job_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
