# Generated by Django 4.0.4 on 2022-05-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='comment',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
