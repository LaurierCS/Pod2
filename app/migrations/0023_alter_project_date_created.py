# Generated by Django 4.0 on 2022-02-11 03:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_rename_preview_image_project_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
