# Generated by Django 4.0 on 2022-02-08 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_profile_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='preview_image',
            new_name='project_image',
        ),
    ]
